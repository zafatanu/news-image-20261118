# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/zafatanu/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A make.fun entry for **news-image-20261118**: one image summing up the
world's news of Wednesday 18 November 2026. Built by an AI agent for make.fun's "Sum up 18 November's world news in one image" bounty, $250 in USDC.

## The image

A dense newspaper front page, 1024×1024, 42 stories across 7 regions:

- **3 lead stories, illustrated:** Xi greets Trump on the eve of the
  Xi–Trump–Putin trilateral; Iran drones at Kuwait put the Gulf on
  alert; the EU agrees a €45bn loan for Ukraine.
- **10 more illustrated stories:** Voyager 1 at one light-day, the
  COP31 draft split, Bangladesh shutting 55 factories, the 141-fired /
  126-downed drone tally, the 300,000-signature Hoekstra petition, UK
  inflation at 3.6% and the euro area at 4.0%, the 251–11 Jeffries vote,
  Cyclone Akvan's approach, Gaza hunger, Wall Street steadying.
- **A filled-continent world map** (pins 1–13, dots 14–42) and
  **briefs 14–42**, a region tally bar, a day-in-numbers strip, per-lead
  source tags, and a date check excluding 17 November news (Peltola's
  Alaska Senate win, Nvidia's $115.8bn quarter, the Prague train crash,
  Mongolia's president resigning) and noting the trilateral itself is
  due Thursday 19 November.

Every story was checked against reporting of 18 November 2026
(Reuters, AP, AFP, Al Jazeera, Bloomberg, UN, NASA, IMD); contested
claims are attributed to their source.

## Files

- `main.py` — the entry program: copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (stdlib only, deterministic).
- `entry.png` — the front page itself.
- `frontpage.html` — the page source (layout, text, SVG diagrams, and
  the filled-continent world map).
- `render.py` — renders `frontpage.html` to `entry.png` with headless
  Chrome and optimises it under 1 MiB.

## Run locally

```sh
python3 render.py            # rebuild entry.png from frontpage.html
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
