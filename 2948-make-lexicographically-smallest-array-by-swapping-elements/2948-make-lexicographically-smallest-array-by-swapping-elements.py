class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        ans = [0] * n
        i = 0

        while i < n:
            j = i + 1

            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            indices = []
            for k in range(i, j):
                indices.append(arr[k][1])

            indices.sort()

            for k in range(i, j):
                ans[indices[k - i]] = arr[k][0]

            i = j

        return ans