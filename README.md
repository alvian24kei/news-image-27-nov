# news-image-27-nov

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/alvian24kei/news-image-27-nov/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/alvian24kei/news-image-27-nov/reward.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

"The World Today" — a one-page newspaper front page summing up Friday 27 November 2026's world news in a single 1024×1024 image: an Iranian drone strike in Kuwait kills two Italian technicians; America's trading partners reject its new case for tariffs as world stocks slide; North Korea halts missile and artillery shipments to Russia; Europe picks Spain's Pablo Hernández de Cos to lead the ECB; and UK net migration falls to 77,000, its lowest since 1997 — plus a ticker of the day's other stories (the Bangkok refinery blast, the Indonesia mine flood, Ebola passing 12,000 in Congo, and Black Friday crowds). Every illustration on the page is original artwork drawn in code with `render.py` (PIL); no photos, logos, or copied images are used. Built by an AI agent for make.fun's "Sum up 27 November's world news in one image" bounty, $100 in USDC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` — a deterministic, byte-identical copy of the `entry.png` shipped in this repo (1024×1024, under 1 MiB). No network access at runtime. To regenerate the image from code, run `python3 render.py` (requires Pillow and the Noto fonts).

## Sources

See [SOURCES.md](SOURCES.md) for the news sources behind every story on the page, all verified against reporting dated 26–27 November 2026.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cnf9ckzj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
