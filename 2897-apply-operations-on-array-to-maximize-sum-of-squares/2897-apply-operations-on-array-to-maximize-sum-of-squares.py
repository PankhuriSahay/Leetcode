class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7

        bit_count = [0] * 31

        # Count occurrence of every bit
        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    bit_count[bit] += 1

        ans = 0

        # Construct k maximum possible numbers
        for _ in range(k):
            x = 0

            for bit in range(31):
                if bit_count[bit] > 0:
                    x |= (1 << bit)
                    bit_count[bit] -= 1

            ans = (ans + x * x) % MOD

        return ans