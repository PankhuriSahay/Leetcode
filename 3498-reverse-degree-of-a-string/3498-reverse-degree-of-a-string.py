class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            reverse_value = 26 - (ord(s[i]) - ord('a'))
            ans += reverse_value * (i + 1)

        return ans
        