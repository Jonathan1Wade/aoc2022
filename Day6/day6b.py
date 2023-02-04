def find_start_of_message(data):
    for i in range(14, len(data)):
        if len(set(data[i-14:i])) == 14:
            return i
    return -1

with open("Day6/input.txt", "r") as f:
    data = f.read().strip()
    result = find_start_of_message(data)
    print("First marker after character", result)
