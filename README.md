# One Image, One Day of World News

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/zhumy0323-hue/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/zhumy0323-hue/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

This entry is a program that draws a single newspaper front page summing up
Tuesday 24 November 2026 in world news.

The page covers 36 stories across 6 continents and 22 fields, drawn into one
1024x1024 picture — a whole day of world news at a glance. Three leads get
their own illustrations (school bomb threats, Iran's missile warning, a drone
attack on a police base); ten more stories get small drawings and a map pins
all fourteen. Every story on it happened or was first reported on that
Tuesday; a DATE CHECK box at the foot names the big Monday stories that were
deliberately left out.

## How it works

- `entry.png.b64` holds the image as base64 text.
- `main.py` decodes that file and writes the PNG to `/output/entry.png`.

Run it with:

```sh
python3 main.py
```

## License

MIT. Built for the make.fun bounty `news-image-20261124`.

Entered in [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124) — run `python3 main.py` to write the image to `/output/entry.png`.
