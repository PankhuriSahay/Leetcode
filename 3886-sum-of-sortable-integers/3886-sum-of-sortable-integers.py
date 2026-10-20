class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        pref_max = [0] * (n + 1)
        suff_min = [float('inf')] * (n + 1)
        drops = [0] * n

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        for i in range(1, n):
            drops[i] = drops[i - 1]
            if nums[i - 1] > nums[i]:
                drops[i] += 1

        def check(k):
            for i in range(0, n, k):
                end = i + k - 1

                count = drops[end] - drops[i]

                if nums[end] > nums[i]:
                    count += 1

                if count > 1:
                    return False

                if pref_max[i] > suff_min[i]:
                    return False

            return True

        k = 1
        while k * k <= n:
            if n % k == 0:
                if check(k):
                    ans += k

                other = n // k
                if other != k and check(other):
                    ans += other

            k += 1

        return ans
