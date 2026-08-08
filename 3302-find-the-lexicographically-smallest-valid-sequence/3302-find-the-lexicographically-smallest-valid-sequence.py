class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[i] = maximum number of characters of word2
        # that can be matched using word1[i:]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                j -= 1
                suf[i] += 1

        ans = []
        j = 0
        mismatch_used = False

        for i in range(n):
            if j == m:
                break

            # Normal matching character
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif not mismatch_used:
                remaining = m - j - 1

                if suf[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

        if j == m:
            return ans

        return []