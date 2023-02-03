def sum_group_of_numbers(input_str):
    groups = input_str.strip().split("\n\n")
    sums = []
    for i, group in enumerate(groups):
        numbers = [int(num) for num in group.split("\n") if num.strip()]
        sums.append((i+1, sum(numbers)))
    top_3_groups = sorted(sums, key=lambda x: x[1], reverse=True)[:3]
    return sum(group[1] for group in top_3_groups)

with open("Day1/input.txt", "r") as file:
    input_str = file.read()

total = sum_group_of_numbers(input_str)
print(f"The total of the top 3 groups is {total}.")
