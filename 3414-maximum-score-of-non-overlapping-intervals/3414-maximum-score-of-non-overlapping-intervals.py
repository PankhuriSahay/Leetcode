class Solution(object):
    def maximumWeight(self, intervals):
        from bisect import bisect_right, insort

        n = len(intervals)

        # (start, end, weight, original_index)
        data = []
        for i in range(n):
            l, r, w = intervals[i]
            data.append((l, r, w, i))

        data.sort()

        starts = [x[0] for x in data]

        # next_index[i] = first interval whose start > current end
        next_index = [0] * n

        for i in range(n):
            r = data[i][1]
            next_index[i] = bisect_right(starts, r)

        # dp_score[k][i]:
        # maximum score using at most k intervals from i onwards
        dp_score = [[0] * (n + 1) for _ in range(5)]

        # indices chosen for that maximum score
        dp_indices = [[()] * (n + 1) for _ in range(5)]

        for i in range(n - 1, -1, -1):
            l, r, weight, original_index = data[i]
            nxt = next_index[i]

            for k in range(1, 5):

                # Option 1: skip current interval
                skip_score = dp_score[k][i + 1]
                skip_indices = dp_indices[k][i + 1]

                # Option 2: take current interval
                take_score = weight + dp_score[k - 1][nxt]

                temp = list(dp_indices[k - 1][nxt])
                insort(temp, original_index)
                take_indices = tuple(temp)

                # Choose higher score.
                # If score is same, choose lexicographically smaller indices.
                if (take_score > skip_score or
                    (take_score == skip_score and
                     take_indices < skip_indices)):

                    dp_score[k][i] = take_score
                    dp_indices[k][i] = take_indices

                else:
                    dp_score[k][i] = skip_score
                    dp_indices[k][i] = skip_indices

        return list(dp_indices[4][0])