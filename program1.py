def num_islands(map):
    if not map:
        return 0

    rows, cols = len(map), len(map[0])
    islands = 0

    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and map[r][c] == 'L':
            map[r][c] = 'W'  # Mark visited landmass as water
            dfs(r-1, c)  # Explore up
            dfs(r+1, c)  # Explore down
            dfs(r, c-1)  # Explore left
            dfs(r, c+1)  # Explore right

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 'L':  # Found new island
                islands += 1
                dfs(r, c)  # Explore and mark island as visited

    return islands

# Test cases
map1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]
print(num_islands(map1))  # Output: 1

map2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]
print(num_islands(map2))  # Output: 3
