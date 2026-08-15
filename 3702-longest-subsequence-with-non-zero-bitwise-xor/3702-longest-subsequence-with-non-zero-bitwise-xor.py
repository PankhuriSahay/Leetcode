class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        xor = 0
        zero_count = 0

        for num in nums:
            xor ^= num

            if num == 0:
                zero_count += 1

        if xor != 0:
            return n

        if zero_count == n:
            return 0

        return n - 1