#!/usr/bin/env python3
"""Export graph seed JSONL to idempotent Neo4j Cypher or CSV-like JSON."""
from __future__ import annotations
import argparse, json, pathlib

def rows(path):
    return [json.loads(x) for x in pathlib.Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]
def cypher_string(s): return json.dumps(str(s), ensure_ascii=False)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1])
    ap.add_argument("--output",type=pathlib.Path)
    a=ap.parse_args(); g=a.root/"11_graph_seed"
    entities=rows(g/"entities.jsonl"); relations=rows(g/"relations.jsonl")
    out=a.output or g/"graph_export.cypher"
    lines=["// CPCS graph seed export. Re-running is idempotent by entity_id/relation_id.",
           "CREATE CONSTRAINT cpcs_entity_id IF NOT EXISTS FOR (n:CPCSEntity) REQUIRE n.entity_id IS UNIQUE;",""]
    for e in entities:
        props={"entity_id":e["entity_id"],"entity_type":e.get("type"),"label":e.get("label"),"attributes_json":json.dumps(e.get("attributes",{}),ensure_ascii=False,sort_keys=True)}
        assignments=", ".join(f"n.{k} = {cypher_string(v)}" for k,v in props.items() if v is not None)
        lines.append(f"MERGE (n:CPCSEntity {{entity_id: {cypher_string(e['entity_id'])}}}) SET {assignments};")
    lines.append("")
    for r in relations:
        attrs=json.dumps(r.get("attributes",{}),ensure_ascii=False,sort_keys=True)
        pred=str(r.get("predicate","RELATED_TO")).upper().replace("-","_")
        if not pred.replace("_","").isalnum(): pred="RELATED_TO"
        lines.append(f"MATCH (a:CPCSEntity {{entity_id: {cypher_string(r['source'])}}}), (b:CPCSEntity {{entity_id: {cypher_string(r['target'])}}}) MERGE (a)-[x:{pred} {{relation_id: {cypher_string(r['relation_id'])}}}]->(b) SET x.attributes_json = {cypher_string(attrs)};")
    out.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"entities":len(entities),"relations":len(relations),"output":str(out)},indent=2))
if __name__=="__main__": main()
