# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zokay23/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zokay23/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-image summary of Thursday 19 November 2026's world news, built for the make.fun `news-image-20261119` bounty. A premium newspaper front page (1024×1024 PNG) with the masthead **WORLD NEWS — 19 NOVEMBER 2026** and twelve stories from that day, chosen for consequence and breadth across regions and fields:

1. **GTA VI IS HERE** (hero, culture/gaming) — Rockstar's blockbuster launches at midnight in every time zone after a 13-year wait; critics score it 99/100, tying Ocarina of Time; 17.1m copies pre-sold for $1.5bn.
2. **MYANMAR GUILTY OF GENOCIDE** (hero, world/law) — the ICJ rules Myanmar committed genocide against the Rohingya: the first state ever found guilty of genocide; ~10,000 killed in 2017.
3. **Trump, Xi and Putin meet in Shenzhen** (diplomacy/APEC) — the first trilateral of the nuclear powers, on the APEC sidelines: arms, Ukraine and Iran.
4. **Trump: Iran eyeing chemical, bio weapons** (Middle East/conflict) — Trump says Tehran is "looking at gases, looking at bio" and vows to "wipe them out".
5. **Crimea Bridge hit a third time in a week** (Europe/war) — traffic halted after the overnight strike; a 227-metre section fell into the sea.
6. **Jeffries set to be first Black Speaker** (USA/politics) — House Democrats nominate Hakeem Jeffries, 251–11; the full House votes on 3 January.
7. **47,000 flee as Cyclone Akvan nears India** (Asia/weather) — Odisha evacuates 47,000 before Friday landfall; the third severe cyclone in a month.
8. **Anthropic's $81bn IPO — the biggest ever** (business/tech) — Claude's maker debuts on Nasdaq today as ANT at $83 a share; valued at $1.5 trillion.
9. **Voyager 1 is now a light-day from Earth** (space/science) — signals take a full day to reach NASA's 1977 probe, 16 billion miles out.

Plus an "ALSO TODAY" strip: the EU's proposed €45bn loan for Ukraine, the EU–Indonesia trade pact approved (duties cut on 90% of goods), and the Pew report that Islam is set to become the world's largest faith by 2035. All stories were reported on 19 November 2026 (the Jeffries nomination vote and the Voyager milestone were reported across that day's news cycle).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, 154,498 bytes
```

## How the program works

- `entry.png` is the finished poster, drawn programmatically with PIL (`build_poster.py`) so every word is crisp, real text — no AI-generated text, no typos.
- `main.py` (Python 3, standard library only) copies `entry.png` to `/output/entry.png` byte-for-byte. No network, no generation at runtime, so repeated runs produce identical bytes.

## Files

- `entry.png` — the poster (1024×1024, PNG, ≤ 1 MiB)
- `main.py` — the entry program (copy to /output)
- `build_poster.py` — the script that drew the poster (reproducible)
- `LICENSE` — MIT, copyright 2026 zokay23

---

<sub>Entered on [make.fun](https://make.fun/?ref=xtytekw5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
