class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Option 1: remove both from the front
        option1 = right + 1

        # Option 2: remove both from the back
        option2 = n - left

        # Option 3: remove one from front and one from back
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)