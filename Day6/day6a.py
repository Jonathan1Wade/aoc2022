def find_start_of_packet(data):
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i
    return -1

with open("Day6/input.txt", "r") as f:
    data = f.read().strip()
    result = find_start_of_packet(data)
    print("First marker after character", result)
