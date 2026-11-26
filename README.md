# Funniest Forecast for a City That Isn't

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/Naiononr/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/Naiononr/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)

A single-line weather forecast for Blorptown, a city that does not exist:
heavy rain of left shoes is expected tonight, and residents are advised
to wear matching pairs indoors. Built for the make.fun competition
"Funniest Forecast for a City That Isn't" — one line, at most 120
characters, judged pairwise by an AI comedy weather editor.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is stdlib-only and deterministic. It honours `MAKEFUN_OUTPUT_DIR`
(default `/output`), writes via a temp file in the same directory with mode
0644, and writes no trailing newline.

---

Built with [make.fun](https://make.fun/r/25acfgqs)
