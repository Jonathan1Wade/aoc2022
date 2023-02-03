def find_badges(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    priorities_sum = 0
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        badge = ''
        for item in set(''.join(group)):
            count = sum([item in line for line in group])
            if count >= 2:
                badge = item
                break
        priority = ord(badge) - 96 if badge.islower() else ord(badge) - 38
        priorities_sum += priority
    return priorities_sum

print(find_badges('Day3/input.txt'))

