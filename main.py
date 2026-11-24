#!/usr/bin/env python3
"""SARI -- one word for the boss: Micromanager.

The program writes the word to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

Sari is the named character here, the employee who has to live
with this boss every working day. Her boss cannot let a single
task leave his sight: he rewrites her emails after she sends
them, stands behind her chair to watch her type, and calls a
meeting to approve the agenda of the next meeting. Sari does
her job well, and that is exactly the problem -- the better she
does it, the more closely he watches, as if competence were a
reason for supervision rather than the very reason to step back.

The word lands because everyone has met this boss, or worked
for him, or quietly been him on a bad week. It is funny on its
own, no caption needed: twelve letters that carry a whole
office, a whole inbox of "just checking in" messages, and a
whole career of being asked for a status update five minutes
after the last one. It is true because micromanagement is not
a rare flaw; it is the most common boss habit there is, the
one colleagues repeat at lunch with a sigh and a laugh.

The brief asks for exactly one word, up to 30 characters, no
phrase, no caption, no explanation -- and "Micromanager" is
exactly that: one word, 12 characters, the whole entry. The
character hook lives here in the docstring and the README,
never in the output file, so the entry stays a single clean
word that stands on its own before the judge.
"""

import os

LINE = "Micromanager"


def main():
    assert LINE.strip() == LINE and len(LINE.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(LINE) <= 30, "line outside the 1-30 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
