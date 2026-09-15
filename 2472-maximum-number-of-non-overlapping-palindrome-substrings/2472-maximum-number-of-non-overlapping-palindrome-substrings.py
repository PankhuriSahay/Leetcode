class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length >= k:
                    dp[right + 1] = max(dp[right + 1],
                                        dp[left] + 1)
                    break

                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length >= k:
                    dp[right + 1] = max(dp[right + 1],
                                        dp[left] + 1)
                    break

                left -= 1
                right += 1

        return dp[n]
        