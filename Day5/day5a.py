import re
import sys
from collections import deque

def main() -> None:
    with open("Day5/input.txt", "r") as f:
        data = f.read()

    grid, instrs = data.split("\n\n")
    grid = grid.split("\n")
    instrs = instrs.strip().split("\n")

    cols: list[deque] = []

    for x in range(max(row.count("[") for row in grid[:-1])):
        col = deque()
        index = x * 4 + 1

        for y in range(len(grid) - 1):
            ch = grid[y][index]
            if ch == " ":
                continue

            col.append(ch)

        cols.append(col)

    for instr in instrs:
        amount, fr, to = map(int, re.findall(r"(\d+)", instr))

        for _ in range(amount):
            cols[to - 1].appendleft(cols[fr - 1].popleft())

    print("".join(col[0] for col in cols))

if __name__ == "__main__":
    main()
