def main():
    with open("Day8/input.txt", "r") as f:
        grid = [list(map(int, line.strip())) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    max_scenic_score = 0

    for row in range(rows):
        for col in range(cols):
            tree_height = grid[row][col]

            up_view = next((i for i in range(row - 1, -1, -1) if grid[i][col] >= tree_height), None)
            up_view = row if up_view is None else row - up_view - 1

            down_view = next((i for i in range(row + 1, rows) if grid[i][col] >= tree_height), None)
            down_view = rows - row - 1 if down_view is None else down_view - row - 1

            left_view = next((j for j in range(col - 1, -1, -1) if grid[row][j] >= tree_height), None)
            left_view = col if left_view is None else col - left_view - 1

            right_view = next((j for j in range(col + 1, cols) if grid[row][j] >= tree_height), None)
            right_view = cols - col - 1 if right_view is None else right_view - col - 1

            scenic_score = up_view * down_view * left_view * right_view
            max_scenic_score = max(max_scenic_score, scenic_score)

    print(max_scenic_score)


if __name__ == "__main__":
    main()