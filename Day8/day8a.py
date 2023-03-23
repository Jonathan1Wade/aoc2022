def main():
    with open("Day8/input.txt", "r") as f:
        grid = [list(map(int, line.strip())) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    visible_trees = 0

    # check edge trees
    visible_trees += rows * 2 + cols * 2 - 4

    # check interior trees
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            tree_height = grid[row][col]
            if all(grid[i][col] < tree_height for i in range(row)) or \
                    all(grid[i][col] < tree_height for i in range(row + 1, rows)) or \
                    all(grid[row][j] < tree_height for j in range(col)) or \
                    all(grid[row][j] < tree_height for j in range(col + 1, cols)):
                visible_trees += 1

    print(visible_trees)


if __name__ == "__main__":
    main()