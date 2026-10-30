class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        import heapq
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')

        dist = [[INF] * (k + 1) for _ in range(n)]

        # At node 0, its label appears once
        dist[0][1] = 0

        heap = [(0, 0, 1)]

        while heap:
            d, u, cnt = heapq.heappop(heap)

            if d != dist[u][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_dist = d + w

                if new_dist < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_dist
                    heapq.heappush(
                        heap,
                        (new_dist, v, new_cnt)
                    )

        return -1
        