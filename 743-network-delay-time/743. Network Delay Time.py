class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, w in times: 
            adj_list[u].append((v, w))
        
        min_heap = [(0, k)]
        shortest_paths = {}
        
        while min_heap: 
            cost, node = heapq.heappop(min_heap)
            if node in shortest_paths: 
                continue
            
            shortest_paths[node] = cost

            for neighbor, cost2 in adj_list[node]:
                if neighbor not in shortest_paths: 
                    heapq.heappush(min_heap, (cost+cost2, neighbor))
        
        return max(shortest_paths.values()) if len(shortest_paths) == n else -1