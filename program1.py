class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
                     if not grid or not grid[0]:
        return 0
class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
       
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # Boundary check or if it's water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            # Mark the cell as visited
            visited[r][c] = True
            # Check all four directions (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    # New island found, initiate DFS
                    dfs(r, c)
                    island_count += 1

        return island_count

# Example usage
solution = Solution()

# Example 1
dispatch1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
print(solution.getTotalIsles(dispatch1))  # Output: 1

# Example 2
dispatch2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"],
]
print(solution.getTotalIsles(dispatch2))  # Output: 3
