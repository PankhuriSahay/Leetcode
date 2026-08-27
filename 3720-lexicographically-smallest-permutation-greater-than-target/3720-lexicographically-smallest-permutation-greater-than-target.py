class Solution(object):
    def lexGreaterPermutation(self, s, target):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        prefix = []

        def build_remaining():
            res = []
            for i in range(26):
                if count[i] > 0:
                    res.append(chr(ord('a') + i) * count[i])
            return ''.join(res)

        n = len(s)

        # Try to match target from left to right
        for i in range(n):
            idx = ord(target[i]) - ord('a')

            if count[idx] > 0:
                prefix.append(target[i])
                count[idx] -= 1
            else:
                # Try smallest character greater than target[i]
                for j in range(idx + 1, 26):
                    if count[j] > 0:
                        count[j] -= 1
                        return ''.join(prefix) + chr(ord('a') + j) + build_remaining()

                # Cannot make it greater here, so backtrack
                break

        # Backtrack to an earlier position and make it slightly greater
        i = len(prefix) - 1

        while i >= 0:
            ch = prefix.pop()
            idx = ord(ch) - ord('a')
            count[idx] += 1

            target_idx = ord(target[i]) - ord('a')

            for j in range(target_idx + 1, 26):
                if count[j] > 0:
                    count[j] -= 1
                    return ''.join(prefix) + chr(ord('a') + j) + build_remaining()

            i -= 1

        return ""