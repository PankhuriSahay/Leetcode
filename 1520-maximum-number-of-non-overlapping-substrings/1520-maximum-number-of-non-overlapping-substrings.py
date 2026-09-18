class Solution(object):
    def maxNumOfSubstrings(self, s):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Store first and last occurrence of every character
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Try to build the smallest valid substring
        # starting from the first occurrence of each character
        for c in range(26):
            if first[c] == n:
                continue

            start = first[c]
            end = last[c]

            i = start
            valid = True

            while i <= end:
                x = ord(s[i]) - ord('a')

                # If this character starts before our interval,
                # then this interval cannot be valid
                if first[x] < start:
                    valid = False
                    break

                # Expand interval if needed
                end = max(end, last[x])
                i += 1

            if valid:
                intervals.append((start, end))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        # Greedily choose non-overlapping intervals
        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans