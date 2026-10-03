"""Unit tests for the TwelveLabs client. Fake clients only: no network, no SDK import."""
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from tlclient import assets, common, embed  # noqa: E402
from tlclient.analyze import analyze_video  # noqa: E402
from tlclient.cli import main as cli_main  # noqa: E402


def asset(i, filename, status="ready", created="2026-09-0%dT00:00:00Z", file_type="video/mp4"):
    return SimpleNamespace(id="a%d" % i, filename=filename, status=status, file_type=file_type,
                           method="direct", size=1000 * i, duration=4.0, created_at=created % i, error=None)


class FakeAssets:
    def __init__(self, items=None):
        self.items = items or []
        self.list_calls = []
        self.create_calls = []
        self.retrieve_statuses = []

    def list(self, **kwargs):
        self.list_calls.append(kwargs)
        name = (kwargs.get("filename") or "").lower()
        types = kwargs.get("asset_types")
        for item in self.items:
            if name and name not in item.filename.lower():
                continue
            if types and item.file_type.split("/")[0] not in types:
                continue
            yield item

    def create(self, **kwargs):
        self.create_calls.append({k: (v if k != "file" else "<file>") for k, v in kwargs.items()})
        return SimpleNamespace(id="new1", filename=kwargs.get("filename"), status="processing",
                               file_type=None, method=kwargs["method"], size=None, duration=None,
                               created_at=None, error=None)

    def retrieve(self, asset_id, **kwargs):
        status = self.retrieve_statuses.pop(0) if self.retrieve_statuses else "ready"
        return SimpleNamespace(id=asset_id, filename="f", status=status, file_type="video/mp4",
                               method="direct", size=1, duration=1.0, created_at=None, error=None)


class FakeMultipart:
    def __init__(self):
        self.calls = []

    def upload_file(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(asset_id="big1", upload_id="u1")


class FakeClient:
    def __init__(self, items=None):
        self.assets = FakeAssets(items)
        self.multipart_upload = FakeMultipart()
        self.analyze_calls = []
        self.embed_calls = []
        outer = self

        class V2:
            def create(self, **kwargs):
                outer.embed_calls.append(kwargs)
                return {"data": [{"embedding": [0.1]}]}

        self.embed = SimpleNamespace(v_2=V2())

    def analyze(self, **kwargs):
        self.analyze_calls.append(kwargs)
        return {"data": "{}", "finish_reason": "stop"}


class SdkAndKey(unittest.TestCase):
    def test_sdk_range_accepts_131_and_135_refuses_older_newer_and_prerelease(self):
        self.assertTrue(common.sdk_compatible("1.3.1"))
        self.assertTrue(common.sdk_compatible("1.3.5"))
        self.assertFalse(common.sdk_compatible("1.2.9"))
        self.assertFalse(common.sdk_compatible("1.4.0"))
        self.assertFalse(common.sdk_compatible("1.3.0b1"))
        self.assertFalse(common.sdk_compatible(None))

    def test_key_from_env_wins_and_is_never_in_doctor_output(self):
        secret = "tlk_SECRET_VALUE"
        report = common.doctor({"TWELVE_LABS_API_KEY": secret}, sdk_version="1.3.5")
        self.assertEqual(report["api_key_source"], "env")
        self.assertTrue(report["ready"])
        self.assertNotIn(secret, repr(report))

    def test_key_from_keychain_on_macos(self):
        calls = []

        def runner(cmd, **kwargs):
            calls.append(cmd)
            return SimpleNamespace(returncode=0, stdout="tlk_FROM_KEYCHAIN\n")

        secret, source = common.resolve_api_key({"USER": "king"}, runner=runner, system="Darwin")
        self.assertEqual((secret, source), ("tlk_FROM_KEYCHAIN", "keychain"))
        self.assertIn("cpcs-twelvelabs-api", calls[0])

    def test_no_key_reports_none_and_not_ready(self):
        runner = lambda cmd, **kw: SimpleNamespace(returncode=44, stdout="")  # noqa: E731
        report = common.doctor(sdk_version="1.3.5",
                               key_lookup=lambda: common.resolve_api_key({"USER": "king"}, runner=runner, system="Darwin"))
        self.assertEqual(report["api_key_source"], "none")
        self.assertFalse(report["ready"])

    def test_embed_model_is_an_explicit_decision(self):
        self.assertEqual(common.resolve_embed_model(None), "marengo3.5")
        self.assertEqual(common.resolve_embed_model("marengo3.0"), "marengo3.0")
        with self.assertRaises(ValueError):
            common.resolve_embed_model("marengo2.7")


class AssetLibrary(unittest.TestCase):
    def setUp(self):
        self.client = FakeClient([asset(1, "intro.mp4"), asset(2, "fight_take2.mp4"),
                                  asset(3, "fight.mp4"), asset(4, "logo.png", file_type="image/png")])

    def test_list_is_newest_first_and_respects_limit(self):
        out = assets.list_assets(limit=3, client=self.client)
        self.assertEqual(len(out), 3)
        self.assertEqual([a["id"] for a in out], sorted([a["id"] for a in out], reverse=True))
        self.assertEqual(self.client.assets.list_calls[0]["page_limit"], 3)

    def test_filters_are_passed_to_the_api(self):
        assets.list_assets(asset_types=["image"], filename="logo", client=self.client)
        call = self.client.assets.list_calls[0]
        self.assertEqual(call["asset_types"], ["image"])
        self.assertEqual(call["filename"], "logo")

    def test_unknown_asset_type_is_refused(self):
        with self.assertRaises(ValueError):
            assets.list_assets(asset_types=["gif"], client=self.client)

    def test_find_puts_exact_filename_first(self):
        out = assets.find_assets("fight.mp4", client=self.client)
        self.assertEqual(out[0]["filename"], "fight.mp4")
        out = assets.find_assets("fight", client=self.client)
        self.assertEqual({a["filename"] for a in out}, {"fight.mp4", "fight_take2.mp4"})


class Uploads(unittest.TestCase):
    def setUp(self):
        self.client = FakeClient()
        self.tmp = Path(tempfile.mkdtemp(prefix="tl_test_"))

    def _file(self, name, size=10):
        p = self.tmp / name
        p.write_bytes(b"0" * size)
        return p

    def test_image_and_video_upload_direct_with_metadata(self):
        out = assets.upload_asset(media_type="image", file_path=self._file("a.png"),
                                  user_metadata={"project": "cpcs", "take": 2}, client=self.client)
        self.assertEqual(out["id"], "new1")
        call = self.client.assets.create_calls[0]
        self.assertEqual(call["method"], "direct")
        self.assertEqual(call["filename"], "a.png")
        self.assertEqual(call["user_metadata"], '{"project": "cpcs", "take": 2}')
        assets.upload_asset(media_type="video", file_path=self._file("b.mp4"), client=self.client)
        self.assertEqual(self.client.assets.create_calls[1]["method"], "direct")

    def test_url_upload(self):
        assets.upload_asset(media_type="video", url="https://example.com/v.mp4", client=self.client)
        self.assertEqual(self.client.assets.create_calls[0]["method"], "url")
        with self.assertRaises(ValueError):
            assets.upload_asset(media_type="video", url="ftp://x/v.mp4", client=self.client)

    def test_large_video_routes_to_multipart(self):
        p = self._file("big.mp4")
        original = dict(assets.DIRECT_LIMIT)
        assets.DIRECT_LIMIT["video"] = 5  # make the 10-byte file count as large
        try:
            out = assets.upload_asset(media_type="video", file_path=p, client=self.client)
        finally:
            assets.DIRECT_LIMIT.update(original)
        self.assertEqual(out["method"], "multipart")
        self.assertEqual(out["id"], "big1")
        self.assertEqual(self.client.multipart_upload.calls[0]["file_type"], "video")
        self.assertEqual(self.client.assets.create_calls, [])

    def test_oversized_image_is_refused_with_the_limit_named(self):
        p = self._file("huge.png")
        original = dict(assets.DIRECT_LIMIT)
        assets.DIRECT_LIMIT["image"] = 5
        try:
            with self.assertRaises(ValueError) as ctx:
                assets.upload_asset(media_type="image", file_path=p, client=self.client)
        finally:
            assets.DIRECT_LIMIT.update(original)
        self.assertIn("limit", str(ctx.exception))

    def test_exactly_one_source_and_known_type(self):
        with self.assertRaises(ValueError):
            assets.upload_asset(media_type="video", client=self.client)
        with self.assertRaises(ValueError):
            assets.upload_asset(media_type="gif", url="https://example.com/a.gif", client=self.client)

    def test_wait_for_asset_polls_until_ready_and_raises_on_failed(self):
        self.client.assets.retrieve_statuses = ["processing", "processing", "ready"]
        out = assets.wait_for_asset("a1", client=self.client, sleep=lambda s: None, poll_interval_s=0)
        self.assertEqual(out["status"], "ready")
        self.client.assets.retrieve_statuses = ["failed"]
        with self.assertRaises(common.TwelveLabsError):
            assets.wait_for_asset("a1", client=self.client, sleep=lambda s: None, poll_interval_s=0)

    def test_guess_media_type(self):
        self.assertEqual(assets.guess_media_type("clip.MOV"), "video")
        self.assertEqual(assets.guess_media_type("https://x.com/p/still.jpeg?sig=1"), "image")
        self.assertIsNone(assets.guess_media_type("notes.xyz"))


class Embeddings(unittest.TestCase):
    def test_marengo35_uses_multi_input_for_everything(self):
        req = embed.build_embed_request("image", asset_id="img1")
        self.assertEqual(req["model_name"], "marengo3.5")
        self.assertEqual(req["input_type"], "multi_input")
        self.assertEqual(req["multi_input"], {"media_sources": [{"media_type": "image", "asset_id": "img1"}]})
        req = embed.build_embed_request("text", text="a punch")
        self.assertEqual(req["multi_input"], {"input_text": "a punch"})

    def test_marengo30_keeps_per_type_bodies(self):
        req = embed.build_embed_request("video", asset_id="v1", model="marengo3.0")
        self.assertEqual(req["input_type"], "video")
        self.assertEqual(req["video"], {"media_source": {"asset_id": "v1"}})

    def test_embedding_dimension_only_on_35_and_only_allowed_values(self):
        self.assertEqual(embed.build_embed_request("text", text="x", embedding_dimension=256)["embedding_dimension"], 256)
        with self.assertRaises(ValueError):
            embed.build_embed_request("text", text="x", embedding_dimension=300)
        with self.assertRaises(ValueError):
            embed.build_embed_request("text", text="x", model="marengo3.0", embedding_dimension=256)

    def test_result_records_the_model(self):
        client = FakeClient()
        out = embed.create_embedding("text", text="x", client=client)
        self.assertEqual(out["model_name"], "marengo3.5")
        self.assertEqual(client.embed_calls[0]["model_name"], "marengo3.5")


class Analysis(unittest.TestCase):
    def test_asset_or_url_exactly_one(self):
        client = FakeClient()
        analyze_video("describe", asset_id="v1", client=client)
        self.assertEqual(client.analyze_calls[0]["video"], {"type": "asset_id", "asset_id": "v1"})
        self.assertEqual(client.analyze_calls[0]["model_name"], "pegasus1.5")
        analyze_video("describe", video_url="https://example.com/v.mp4", client=client)
        self.assertEqual(client.analyze_calls[1]["video"]["type"], "url")
        with self.assertRaises(ValueError):
            analyze_video("describe", client=client)

    def test_images_switch_to_prompt_v2_and_must_be_referenced(self):
        client = FakeClient()
        analyze_video("does the bottle match <@ref>?", asset_id="v1", images={"ref": "img9"}, client=client)
        call = client.analyze_calls[0]
        self.assertNotIn("prompt", call)
        self.assertEqual(call["prompt_v_2"]["media_sources"], [{"name": "ref", "media_type": "image", "asset_id": "img9"}])
        with self.assertRaises(ValueError):
            analyze_video("no placeholder", asset_id="v1", images={"ref": "img9"}, client=client)

    def test_clip_window_needs_four_seconds(self):
        with self.assertRaises(ValueError):
            analyze_video("x", asset_id="v1", start_s=0, end_s=2, client=FakeClient())


class Cli(unittest.TestCase):
    def test_bad_metadata_returns_error_code_without_traceback(self):
        err = io.StringIO()
        old = sys.stderr
        sys.stderr = err
        try:
            code = cli_main(["upload", "image", "--url", "https://example.com/a.png", "--metadata", "novalue"])
        finally:
            sys.stderr = old
        self.assertEqual(code, 1)
        self.assertIn("KEY=VALUE", err.getvalue())


if __name__ == "__main__":
    unittest.main()
