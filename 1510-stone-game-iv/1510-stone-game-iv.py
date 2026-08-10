class Solution(object):
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            i = 1

            while i * i <= stones:
                remaining = stones - i * i

                if dp[remaining] == False:
                    dp[stones] = True
                    break

                i += 1

        return dp[n]