def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

def find_error(contents):
    n = len(contents) // 2
    first = set(contents[:n])
    second = set(contents[n:])
    return first & second

def sum_of_priorities(contents):
    errors = find_error(contents)
    return sum(get_priority(c) for c in errors)

def main():
    with open("Day3/input.txt", "r") as f:
        contents = [line.strip() for line in f]

    total = 0
    for content in contents:
        total += sum_of_priorities(content)

    print(total)

if __name__ == '__main__':
    main()
