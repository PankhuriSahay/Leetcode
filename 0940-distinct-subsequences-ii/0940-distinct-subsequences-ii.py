class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 1000000007

        end = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            total = sum(end) % MOD

            end[idx] = (total + 1) % MOD

        return sum(end) % MOD