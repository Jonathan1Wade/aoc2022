def parse_multi_string(input_string, sep=","):
    lines = input_string.strip().split("\n")
    arr = [line.strip().split(sep) for line in lines]
    return arr

with open("Day4/input.txt") as f:
    input_string = f.read()

arr = parse_multi_string(input_string)

ans = 0
for a in arr:
    p1 = [int(x) for x in a[0].split("-")]
    p2 = [int(x) for x in a[1].split("-")]
    if ((p1[0] <= p2[0]) and (p1[1] >= p2[1])) or ((p2[0] <= p1[0]) and (p2[1] >= p1[1])):
        ans += 1

print(ans)
