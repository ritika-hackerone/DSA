from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        # Store all indices for each value
        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        # BFS
        queue = deque([0])
        visited = set([0])

        steps = 0

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                # Reached last index
                if curr == n - 1:
                    return steps

                neighbors = []

                # i - 1
                if curr - 1 >= 0:
                    neighbors.append(curr - 1)

                # i + 1
                if curr + 1 < n:
                    neighbors.append(curr + 1)

                # same value indices
                neighbors.extend(graph[arr[curr]])

                for nxt in neighbors:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                # IMPORTANT:
                # Clear to avoid revisiting same-value nodes
                graph[arr[curr]].clear()

            steps += 1