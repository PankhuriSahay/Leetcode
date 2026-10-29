class Solution:
    def palindromePath(self, n, edges, s, queries):

        graph = [[] for _ in xrange(n)]

        for e in edges:
            u = e[0]
            v = e[1]
            graph[u].append(v)
            graph[v].append(u)

        # -------------------------------
        # Build parent, depth, and order
        # -------------------------------

        parent = [-1] * n
        depth = [0] * n
        order = []

        stack = [0]
        parent[0] = -2

        while stack:
            u = stack.pop()
            order.append(u)

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

        parent[0] = -1

        # -------------------------------
        # Subtree sizes + heavy child
        # -------------------------------

        size = [1] * n
        heavy = [-1] * n

        for idx in xrange(len(order) - 1, -1, -1):
            u = order[idx]
            best = 0

            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]

                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        # -------------------------------
        # Heavy-Light Decomposition
        # -------------------------------

        head = [0] * n
        pos = [0] * n

        cur = 0
        chains = [(0, 0)]

        while chains:
            u, h = chains.pop()

            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        chains.append((v, v))

                u = heavy[u]

        # -------------------------------
        # Fenwick Tree for XOR
        # -------------------------------

        bit = [0] * (n + 1)

        def bit_update(i, val):
            i += 1

            while i <= n:
                bit[i] ^= val
                i += i & -i

        def prefix_xor(i):
            res = 0
            i += 1

            while i > 0:
                res ^= bit[i]
                i -= i & -i

            return res

        def range_xor(l, r):
            if l == 0:
                return prefix_xor(r)

            return prefix_xor(r) ^ prefix_xor(l - 1)

        # -------------------------------
        # Insert initial characters
        # -------------------------------

        masks = [0] * n

        for i in xrange(n):
            mask = 1 << (ord(s[i]) - ord('a'))
            masks[i] = mask
            bit_update(pos[i], mask)

        # -------------------------------
        # XOR along path u -> v
        # -------------------------------

        def path_xor(u, v):
            res = 0

            while head[u] != head[v]:

                if depth[head[u]] < depth[head[v]]:
                    temp = u
                    u = v
                    v = temp

                res ^= range_xor(
                    pos[head[u]],
                    pos[u]
                )

                u = parent[head[u]]

            if depth[u] > depth[v]:
                temp = u
                u = v
                v = temp

            res ^= range_xor(
                pos[u],
                pos[v]
            )

            return res

        # -------------------------------
        # Process queries
        # -------------------------------

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":

                u = int(parts[1])
                ch = parts[2]

                new_mask = 1 << (ord(ch) - ord('a'))

                # Remove old char and add new char
                diff = masks[u] ^ new_mask

                bit_update(pos[u], diff)

                masks[u] = new_mask

            else:

                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                # At most one odd-frequency character
                if (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)

        return ans