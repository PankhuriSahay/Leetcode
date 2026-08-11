class Solution(object):
    def missingInteger(self, nums):
        prefix_sum = nums[0]

        # Find the sum of the longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        # Store elements for fast lookup
        elements = set(nums)

        # Find the smallest missing integer
        answer = prefix_sum

        while answer in elements:
            answer += 1

        return answer
    
        # Find the smallest missing integer
        answer = prefix_sum

        while answer in elements:
            answer += 1

        return answer