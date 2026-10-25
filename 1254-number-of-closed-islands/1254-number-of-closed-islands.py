class Solution(object):
    def closedIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == 1:
                return

            grid[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Remove all islands connected to the border
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)

            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)

        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)

            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)

        # Count remaining closed islands
        count = 0

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)

        return count
        