class Solution(object):
    def minOperations(self, s):
        n = len(s)

        # Already sorted
        if all(s[i] >= s[i - 1] for i in range(1, n)):
            return 0

        # For length 2, sorting the whole string is forbidden
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # One operation is enough
        if s[0] == mn or s[-1] == mx:
            return 1

        # Two operations are enough
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Otherwise, 3 operations are required
        return 3
        