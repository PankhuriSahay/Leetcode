class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted(x * x for x in nums)

        n = len(squares)
        negative_count = n // 2

        ans = 0

        for i in range(negative_count):
            ans -= squares[i]

        for i in range(negative_count, n):
            ans += squares[i]

        return ans