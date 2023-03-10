import sys

def main() -> None:
    with open("Day2/input.txt", "r") as f:
        data = f.read().strip()

    s = 0
    for line in data.splitlines():
        a, b = line.split(" ")

        if a == "A":
            s += {
                "X": 1 + 3,
                "Y": 2 + 6,
                "Z": 3 + 0
            }[b]
        elif a == "B":
            s += {
                "X": 1 + 0,
                "Y": 2 + 3,
                "Z": 3 + 6
            }[b]
        elif a == "C":
            s += {
                "X": 1 + 6,
                "Y": 2 + 0,
                "Z": 3 + 3
            }[b]

    print(s)

if __name__ == "__main__":
    main()




