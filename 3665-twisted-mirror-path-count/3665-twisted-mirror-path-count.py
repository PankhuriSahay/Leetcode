class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        # down[j] = ways currently flowing downward into column j
        down = [0] * n
        down[0] = 1

        for i in range(m):
            right = 0

            for j in range(n):

                if grid[i][j] == 1:
                    # Mirror:
                    # left-flow turns down
                    # top-flow turns right
                    right, down[j] = down[j], right

                else:
                    # Normal cell:
                    # both incoming flows combine
                    total = (right + down[j]) % MOD

                    right = total
                    down[j] = total

        return right