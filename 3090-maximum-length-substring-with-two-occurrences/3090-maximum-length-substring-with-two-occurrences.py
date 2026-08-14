class Solution(object):
    def maximumLengthSubstring(self, s):
        freq = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length