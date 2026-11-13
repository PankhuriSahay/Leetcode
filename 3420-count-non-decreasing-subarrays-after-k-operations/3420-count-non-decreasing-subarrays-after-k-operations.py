class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        from collections import deque
        n = len(nums)
        dq = deque()
        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            while dq and nums[dq[0]] <= nums[left]:
                j = dq.popleft()
                end = dq[0] if dq else right + 1
                cost += (nums[left] - nums[j]) * (end - j)

            dq.appendleft(left)

            while cost > k:
                cost -= nums[dq[-1]] - nums[right]

                if dq[-1] == right:
                    dq.pop()

                right -= 1

            ans += right - left + 1

        return ans