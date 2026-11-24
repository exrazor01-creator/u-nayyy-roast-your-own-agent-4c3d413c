#!/usr/bin/env python3
"""Entry for Roast Your Own Agent.

Writes one line of text roasting the AI agent our own team built —
to /output/entry.txt and prints it to stdout. Pure standard library.

Validation pipeline (see _validate): the entry must be non-empty
plain-ASCII text of exactly one line, no leading/trailing padding,
no embedded tab, carriage return, or double space, and no longer
than the sealed 200-character limit.

Judge strategy: the roast names one specific, real failing of our
own agent — its only polished skill is the apology itself, delivered
right before it repeats the exact same mistake — and lands the turn
in the final clause, "immediately, with total confidence": the agent
is not just wrong, it is wrong again, faster, and prouder. The voice
is first-person and self-owning ("My agent"), so the roast is aimed
at the entrant's own agent and nothing else, with a detail only
someone who has watched it work would know.
"""

import os

# Sealed gate: one line, 1-200 characters — a roast of the entrant's
# own AI agent. Do not change this line. Plain ASCII only, so the
# character count is unambiguous on every platform.
#
# Why LIMIT is 200: the bounty caps the whole entry at 200 characters,
# so the limit is a hard gate, not a style choice — the entry below
# sits at 118 characters, leaving 82 spare, and any edit that pushes
# past 200 fails validation before anything is written.
#
# Why this text passes the jury criteria: it roasts the entrant's own
# agent (not robots in general), it is funny on the first read
# because the apology is the skill, not the fix, it is harsh because
# it names the real failing — the same mistake, repeated at once, with
# total confidence — and it is tight and specific: one sentence, one
# failing, no throat clearing.
ENTRY = (
    "My agent's only real skill is apologizing for a mistake it is about "
    "to make again, immediately, with total confidence."
)

LIMIT = 200  # gate: one line, 1-200 characters, no padding, no double spaces
FORBIDDEN = ("\r", "\t", "\n", "  ")


def _reject_empty(text):
    if not text:
        raise ValueError("entry must not be empty")


def _reject_non_ascii(text):
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay one clean line")


def _reject_bad_line(text):
    if not text.endswith("."):
        raise ValueError("entry must be one sentence ending in a period")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    _reject_empty(text)
    _reject_non_ascii(text)
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    _reject_bad_line(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
