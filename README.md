# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zokay23/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zokay23/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-image summary of Thursday 19 November 2026's world news, built for the make.fun `news-image-20261119` bounty. A premium newspaper front page (1024×1024 PNG) with the masthead **WORLD NEWS — 19 NOVEMBER 2026** and six stories from that day, chosen for consequence and breadth across regions and fields:

1. **GTA VI IS HERE** (hero, culture/gaming) — Rockstar's blockbuster launches at midnight in every time zone after a 13-year wait; critics score it 99/100.
2. **World court rules on Rohingya genocide** (world/law) — the ICJ delivers its verdict in Gambia v. Myanmar, the first time it could hold a state guilty of genocide.
3. **Jeffries set to be first Black Speaker** (USA/politics) — House Democrats nominate Hakeem Jeffries; he takes the gavel on 3 January.
4. **Cyclone Akvan bears down on India** (Asia/weather) — the severe storm nears the Andhra Pradesh and Odisha coasts; states on red alert.
5. **US–Iran strikes widen across the Gulf** (Middle East/conflict) — Iran hits a US base in Kuwait and Bahrain again; the US struck a missile site on Qeshm Island.
6. **Voyager 1 reaches a light-day from Earth** (space/science) — after nearly 50 years in space, NASA's probe crosses a record distance.

Plus an "ALSO TODAY" strip: the EU's proposed €45bn loan for Ukraine, and the Pew report that Islam is set to become the world's largest faith by 2035. All stories were reported on 19 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG, 136,021 bytes
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
