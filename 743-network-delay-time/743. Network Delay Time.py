class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, w in times: 
            adj_list[u].append((v,w))

        heap = [(0, k)]
        shortest_paths = {}

        while heap: 
            w1, u1 = heapq.heappop(heap)
            if u1 in shortest_paths: 
                continue
            
            shortest_paths[u1] = w1

            for u2, w2 in adj_list[u1]:
                if u2 not in shortest_paths:
                    heapq.heappush(heap, (w2+w1, u2))
     
        
        return max(shortest_paths.values()) if len(shortest_paths) == n else -1
                     