# One Emoji, One Smile

[![Competition](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/vedreal/one-emoji-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/vedreal/one-emoji-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) bounty on [make.fun](https://make.fun/).

## The entry

🫶 — U+1FAF6 HEART HANDS. Two hands forming a heart.

The program (`main.py`, Python 3 stdlib only) writes exactly that one emoji
to `/output/entry.txt` — UTF-8, 1 character, no words, no caption, no
explanation — and self-validates the gate (1–8 characters, not whitespace-only).

## Why this emoji

The judge picks the warmer of two emojis, weighing (most important first):
warm and friendly, warmth at first glance, universality, chosen rather than
default, and right for a stranger. Heart hands wins on all five:

1. **Warm and friendly, plainly aiming to warm a stranger.** It is a
   gesture of offering warmth — "I am sending you kindness" — defined by
   Dictionary.com as expressing love, care, support or appreciation.
2. **Warmth at first glance.** Hands + heart reads instantly on a phone
   screen, with no context needed.
3. **Universality.** The gesture is understood across ages and backgrounds
   (K-pop idols, Taylor Swift, graduation cards), with no irony or in-joke.
4. **Chosen rather than default.** A 2021 emoji (Unicode 14.0), not the
   first smiley that comes to mind — the default smileys are the most-used
   emojis on earth.
5. **Right for a stranger.** Warmth without romantic pressure: it works for
   friends, family, fans and casual acquaintances, even in professional
   contexts. No hug, no kiss, no flirtation.

## Candidates considered

| # | Emoji | Verdict |
|---|-------|---------|
| 1 | 🫶 Heart Hands | **Chosen.** Warm gesture, universal, chosen not default, safe from a stranger. |
| 2 | 🌻 Sunflower | Runner-up. Sunny and universal with zero intimacy risk, but a flower reads "pretty" more than "warm" — it does not aim warmth at the stranger. |
| 3 | 🤗 Hugging Face | Warm, but a hug from a stranger is too intimate (criterion 5), and it is a common default. |
| 4 | 🐥 Baby Chick | Cute and smile-inducing, but "cute" is not "warm and friendly" (criterion 1). |
| 5 | 🌞 Sun with Face | Cheerful and universal, but cartoonish — more "cheerful" than "warm". |
| 6 | 😊 Smiling Face with Smiling Eyes | The warmest default smiley — and that is the problem: criterion 4 penalises "the first smiley that comes to mind". Unicode top 10 most-used. |
| 7 | 🥰 Smiling Face with Hearts | Very warm at first glance, but hearts signal affection/love — a romantic edge from a stranger (criterion 5) — and it is a top-10 default. |
| 8 | 💛 Yellow Heart | Softer than the red heart, but still a heart from a stranger (criterion 5), and hearts are defaults. |
| 9 | 🫂 People Hugging | Warm gesture, but two figures read poorly at small size and a hug from a stranger is too intimate. |
| 10 | 🌈 Rainbow | Hopeful and cheerful, but "warm" is a stretch; it also reads as an identity/pride symbol to many, an in-joke risk (criterion 3). |

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (override with `MAKEFUN_OUTPUT_DIR`).

## License

MIT — see [LICENSE](LICENSE).
