class Solution:
    def getTotalIsles(self, map_grid: list[list[str]]) -> int:
        # Return 0 if map is empty
        if not map_grid or not map_grid[0]:
            return 0

        # Initialize dimensions and visited cells tracker
        num_rows, num_cols = len(map_grid), len(map_grid[0])
        visited_cells = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        # Helper function to explore connected land cells
        def explore_island(row, col):
            # Stop if out of bounds, cell is water, or already visited
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols or map_grid[row][col] == 'W' or visited_cells[row][col]:
                return
            # Mark current cell as visited
            visited_cells[row][col] = True
            # Recursively explore all adjacent cells (up, down, left, right)
            explore_island(row + 1, col)  # Down
            explore_island(row - 1, col)  # Up
            explore_island(row, col + 1)  # Right
            explore_island(row, col - 1)  # Left

        # Initialize island counter
        total_islands = 0
        # Iterate over each cell in the map grid
        for row in range(num_rows):
            for col in range(num_cols):
                # If an unvisited land cell is found, start exploring a new island
                if map_grid[row][col] == 'L' and not visited_cells[row][col]:
                    explore_island(row, col)
                    total_islands += 1  # Count the new island

        return total_islands

# Example usage
solution = Solution()

# Example 1
map1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
print(solution.getTotalIsles(map1))  # Output: 1

# Example 2
map2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]
print(solution.getTotalIsles(map2))  # Output: 3
