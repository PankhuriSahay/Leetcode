class Solution(object):
    def sumCounts(self, nums):
        ans = 0
        n = len(nums)

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])

                count = len(distinct)
                ans += count * count

        return ans