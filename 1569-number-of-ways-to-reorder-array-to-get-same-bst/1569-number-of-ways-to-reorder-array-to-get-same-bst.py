class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            leftWays = dfs(left)
            rightWays = dfs(right)

            n = len(left) + len(right)
            k = len(left)

            ways = 1
            for i in range(1, k + 1):
                ways = ways * (n - i + 1) // i

            return ways * leftWays * rightWays % MOD

        return (dfs(nums) - 1) % MOD
