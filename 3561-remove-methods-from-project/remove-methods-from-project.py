from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Create adjacency list
        edges = [[] for _ in range(n)]
        in_degree = [0] * n

        # Build graph
        for u, v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        # BFS from suspicious method k
        queue = deque([k])
        suspicious = bytearray(n)
        suspicious[k] = 1

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1
                if suspicious[v] == 0:
                    suspicious[v] = 1
                    queue.append(v)

        # Check whether any suspicious method is still called
        # by a non-suspicious method
        can_remove_all = True
        for i in range(n):
            if suspicious[i] and in_degree[i] > 0:
                can_remove_all = False
                break

        if can_remove_all:
            return [i for i in range(n) if not suspicious[i]]
        else:
            return list(range(n))
