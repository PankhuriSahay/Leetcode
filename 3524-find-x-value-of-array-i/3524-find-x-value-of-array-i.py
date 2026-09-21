class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k

        # dp[r] = number of subarrays ending at previous index
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            rem = num % k

            # Subarray containing only current number
            new_dp[rem] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            # Add all subarrays ending here to final result
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result