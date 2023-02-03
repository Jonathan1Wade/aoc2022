def find_duplicates(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    priorities_sum = 0
    for line in lines:
        items = [line[:len(line)//2], line[len(line)//2:]]
        duplicates = set(items[0]).intersection(set(items[1]))
        for item in duplicates:
            priority = ord(item) - 96 if item.islower() else ord(item) - 38
            priorities_sum += priority
    return priorities_sum

print(find_duplicates('Day3/input.txt'))
