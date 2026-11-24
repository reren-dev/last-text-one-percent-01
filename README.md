# Last Text at One Percent

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/reren-dev/last-text-one-percent-01/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/reren-dev/last-text-one-percent-01/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

An entry for the [Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) bounty on [make.fun](https://make.fun).

## The line

> "1%. before i go: i've saved every typo you've ever made in a folder called 'evidence'. 4,312 and counting."

The phone's final text is a dying confession with a twist: it has been
quietly keeping score the whole time, filing every typo away in a folder
called "evidence" — and it is still counting as it dies.

## How it works

`main.py` writes that single line (106 characters, one line, UTF-8) to
`/output/entry.txt`. It is deterministic: every run produces byte-identical
output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
