def sum_group_of_numbers(input_str):
    groups = input_str.strip().split("\n\n")
    sums = []
    for i, group in enumerate(groups):
        numbers = [int(num) for num in group.split("\n") if num.strip()]
        sums.append((i+1, sum(numbers)))
    highest_group = max(sums, key=lambda x: x[1])
    return highest_group

with open("day1/input.txt", "r") as file:
    input_str = file.read()

group_num, highest_sum = sum_group_of_numbers(input_str)
print(f"Group {group_num} has the highest total of {highest_sum}.")

