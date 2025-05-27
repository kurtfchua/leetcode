class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for src, dst, time in times: 
            adj_list[src].append((dst, time))
        
        min_heap = [(0, k)]
        shortest_paths = {}

        while min_heap: 
            time1, node = heapq.heappop(min_heap) 
            if node in shortest_paths: 
                continue
            shortest_paths[node] = time1

            for dst, time2 in adj_list[node]:
                if dst not in shortest_paths: 
                    heapq.heappush(min_heap, (time2 + time1, dst))

        return max(shortest_paths.values()) if len(shortest_paths) == n else -1       