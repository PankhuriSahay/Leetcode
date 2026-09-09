class Solution(object):
    def countCommas(self, n):
        total = 0
        threshold = 1000

        while threshold <= n:
            total += n - threshold + 1
            threshold *= 1000

        return total
        