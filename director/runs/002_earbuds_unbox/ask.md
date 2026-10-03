# Run 002 — earbuds unboxing

## Ask

> A man unboxes a pair of wireless earbuds at a desk, opens the charging case and puts one earbud
> in his ear, 8 seconds, shot on a phone held by a friend.

Target model: seedance (route unconfirmed; 2,000-character budget from third-party API docs, see
`profiles/seedance.yaml`).

## Intent brief

Locked by the user: one man; a desk; a pair of wireless earbuds in a box; three actions in order
(unbox, open the charging case, put one earbud in his ear); 8 seconds; shot on a phone that a
friend holds. Open: who he is, the box and case design, the room, aspect ratio, the look.
Implied: a hinged-lid charging case; a casual, real-looking clip rather than an ad; the friend
stays off screen.

Two forced decisions. (1) The friend holds the phone, so both of his hands are free and the
camera is a handheld catalog move, not the selfie treatment. (2) Three physical tasks in 8 s
overloaded the clock when every task got the run-001 reading times (12 beats, 9.8 s); resolved in
the open, see `open.jsonl` and `decisions.jsonl` d001. A third forced choice: the ear is the
expensive frame (`HANDS_CONTACT_MANIPULATION.md` §2.3, §5), so the insertion is carried as an
occluded contact (hand and side of head), not a close-up.

## Pass plan summary

Active: intent, entity, interaction, physics, continuity, time, performance, camera, style,
synthesis. Inactive with reason: world (covered by interaction: box lid, case lid and earbud are
the only state changes), action (covered by interaction stages), staging (one actor on screen,
fixed desk layout in the entity text), attention (nothing withheld), light_color (available
indoor light stated in capture texture), audio (not asked; no dialogue).
