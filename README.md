# Sum up 24 November's world news in one image

A single 1024x1024 front-page image that sums up Tuesday 24 November
2026 in world news: 36 stories across 6 continents and 22 fields.

## What is on the page

- **3 lead stories** — the day's biggest headlines, up top.
- **10 small stories** — each with its own illustration and a
  verification badge (CONFIRMED / OFFICIAL / REPORTED).
- **23 more in brief** — a wire list of the rest of the day, kept
  short so every headline fits on one line.
- **UTC timeline** — 7 timed events in order through the day.
- **Figures strip, region bar, and a world map** with 14 numbered pins
  placing the stories on the globe.
- **DATE CHECK box** — states what the page covers (24 November only)
  and what it deliberately leaves out.

Every story was first reported on 24 November 2026 (UTC), cross-checked
against Reuters, AP, AFP, UN News, and other wires.

## Run it

```sh
python3 main.py
```

That decodes `entry.png.b64` and writes the image to
`/output/entry.png`. Only the Python standard library is used.

## License

MIT — see `LICENSE`.
