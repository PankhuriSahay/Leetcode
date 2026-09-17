class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        best = [INF] * n
        left = 0
        current_sum = 0
        min_length = INF
        answer = INF

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                min_length = min(min_length, length)

            best[right] = min_length

        if answer == INF:
            return -1

        return answer
        