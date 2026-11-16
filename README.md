# tiny-chess-01

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/competitions/tiny-chess-01)
[![Rank](https://make.fun/badge/tiny-chess-01/edihartono180102-sys/makefun-tiny-chess-01-edi-20261116/rank.svg)](https://make.fun/competitions/tiny-chess-01)
[![Reward](https://make.fun/badge/tiny-chess-01/edihartono180102-sys/makefun-tiny-chess-01-edi-20261116/reward.svg)](https://make.fun/competitions/tiny-chess-01)

Make.fun competition entry for **tiny-chess-01** (original implementation, built for this repo). Python 3.13 chess engine (`main.py`, stdlib only) that plays through the Make.fun env API (`MAKEFUN_ENV_URL`) with deterministic, bounded search (no clock). No model calls, no external network beyond the env.

## About
- Repository: `edihartono180102-sys/makefun-tiny-chess-01-edi-20261116`
- Competition page: https://make.fun/competitions/tiny-chess-01
- Entrypoint: `main.py` (<= 4096 bytes). Repo snapshot kept under 8192 bytes.

## Notes
- Deterministic behavior; follows env protocol (`/game`, `/move`).
- GitHub repo About should include a make.fun website link and the topic `makefun` before submission (per competition requirements).
