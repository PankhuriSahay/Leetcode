class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        pos = nums.index(0)
        ans = float('inf')

        increasing = True
        decreasing = True

        for i in range(n):
            if nums[(pos + i) % n] != i:
                increasing = False

            if nums[(pos - i) % n] != i:
                decreasing = False

        if increasing:
            ans = min(ans, pos, n - pos + 2)

        if decreasing:
            ans = min(ans, pos + 2, n - pos)

        if ans == float('inf'):
            return -1

        return ans

        