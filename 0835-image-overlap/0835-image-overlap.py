class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        shifts = {}

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        max_overlap = 0

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x2 - x1, y2 - y1)

                shifts[shift] = shifts.get(shift, 0) + 1

                max_overlap = max(max_overlap, shifts[shift])

        return max_overlap
        