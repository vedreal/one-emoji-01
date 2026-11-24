"""One Emoji, One Smile — make.fun entry.

The task: send exactly one emoji, the one most likely to make a
stranger smile. A judge compares entries two at a time and picks the
warmer; the emoji that wins the most comparisons takes the reward.

Chosen entry: U+1FAF6 HEART HANDS.

Why this one, against the judge's brief (most important first):

1. Warm and friendly, plainly aiming to warm a stranger. Two hands
   forming a heart is a gesture of offering warmth — it says "I am
   sending you kindness", not "look at my face". Dictionary.com
   defines it as expressing love, care, support or appreciation.
2. Warmth at first glance. The shape reads instantly on a phone
   screen: hands + heart, no context needed, gently warm rather
   than loud.
3. Universality. The gesture is understood across ages and
   backgrounds — K-pop idols, Taylor Swift, graduation cards,
   birthday posts — with no irony or in-joke that could land wrong.
4. Chosen rather than default. It is a 2021 emoji (Unicode 14.0),
   not the first smiley that comes to mind. The defaults — the
   smiling face with smiling eyes, the slightly smiling face, the
   red heart — are the most-used emojis on earth; this one feels
   picked for the moment while staying instantly readable.
5. Right for a stranger. It carries warmth without romantic
   pressure: it works for friends, family, fans and casual
   acquaintances alike, and is acceptable even in professional
   contexts. No hug (too intimate from a stranger), no kiss, no
   flirtation.

The program writes exactly that one emoji to /output/entry.txt.
"""

import os

# U+1FAF6 HEART HANDS — two hands forming a heart.
EMOJI = "\U0001FAF6"


def output_dir() -> str:
    """Directory the entry file goes in (override for local runs)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry() -> str:
    """Write the single emoji to entry.txt and return its path."""
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    return path


def validate_entry(path: str) -> str:
    """Read the entry back and enforce the bounty gate.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 8 characters, not only white space. This entry is exactly
    one emoji: a single code point, so it passes with room to spare.
    """
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    if not text or text.strip() == "":
        raise ValueError("entry is empty or only white space")
    if not 1 <= len(text) <= 8:
        raise ValueError(f"entry is {len(text)} characters, gate needs 1-8")
    if text != EMOJI:
        raise ValueError("entry does not match the chosen emoji")
    return text


if __name__ == "__main__":
    entry_path = write_entry()
    entry = validate_entry(entry_path)
    print(f"wrote {entry_path}: {entry} ({len(entry)} character)")

