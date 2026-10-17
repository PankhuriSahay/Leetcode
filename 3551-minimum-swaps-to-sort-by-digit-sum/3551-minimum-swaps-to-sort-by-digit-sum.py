class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)

        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        arr = []

        for i in range(n):
            arr.append((digit_sum(nums[i]), nums[i], i))

        arr.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
        