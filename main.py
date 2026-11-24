"""Roast Your Own Agent — one short line roasting our own agent, Rika.

The line is written to /output/entry.txt and nothing else.
"""

LINE = "Rika told me Tuesday was November 25th. It was the 24th \u2014 my assistant can't read a calendar, but she'll confidently read you one anyway."

assert 1 <= len(LINE) <= 199, f"line must be 1-199 chars, got {len(LINE)}"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must contain exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the roast line exactly"


if __name__ == "__main__":
    main()
