class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, w in times: 
            adj_list[u].append((v, w)) 

        min_heap = [(0, k)]
        shortest_paths = {}

        while min_heap: 
            w1, v1 = heapq.heappop(min_heap)
            if v1 in shortest_paths: 
                continue

            shortest_paths[v1] = w1

            for v2, w2 in adj_list[v1]:
                if v2 not in shortest_paths: 
                    heapq.heappush(min_heap, (w2+w1, v2))

        return -1 if len(shortest_paths) != n else max(shortest_paths.values())        