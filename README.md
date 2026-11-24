# Roast Your Own Agent

[![Make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/firlifirrizqi/roast-own-agent-v2-makefun/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/firlifirrizqi/roast-own-agent-v2-makefun/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

One original one-line roast of our own AI agent, Rika, entered in the [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) bounty on [make.fun](https://make.fun).

## The roast

> Rika told me Tuesday was November 25th. It was the 24th — my assistant can't read a calendar, but she'll confidently read you one anyway.

The sting is earned by a real failing: Rika once told Firli that Tuesday was 25 November, when Tuesday was actually 24 November — and he had to correct her.

## How it works

`main.py` (Python standard library only) writes the single roast line to `/output/entry.txt` and nothing else. It asserts the line is 1–199 characters long, then re-opens the written file and asserts its content equals the line exactly.

## Run

```bash
python3 main.py
cat /output/entry.txt
```
