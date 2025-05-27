class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, w in times: 
            adj_list[u].append((v, w))
        
        shortest_paths = {}
        min_heap = [(0, k)]

        while min_heap:
            w1, v1 = heapq.heappop(min_heap)
            if v1 in shortest_paths:
                continue
            shortest_paths[v1] = w1

            for v2, w2 in adj_list[v1]:
                heapq.heappush(min_heap, (w2+w1, v2))
        
        return max(shortest_paths.values()) if len(shortest_paths) == n else -1
