import heapq
from typing import List, Tuple, Union

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        minHeap = [(0, src, k + 1)]
        dist = [[float('inf') for _ in range(k + 2)] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        dist[src][k + 1] = 0

        while minHeap:
            d, u, stops = heapq.heappop(minHeap)
            if u == dst:
                return d
            if stops > 0:
                for v, w in graph[u]:
                    newDist = d + w
                    if newDist < dist[v][stops - 1]:
                        dist[v][stops - 1] = newDist
                        heapq.heappush(minHeap, (newDist, v, stops - 1))

        return -1
