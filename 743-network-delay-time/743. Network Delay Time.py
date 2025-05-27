class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for src, dst, time in times: 
            adj_list[src].append((dst, time))

        min_heap = [(0, k)]
        shortest_map = {}

        while min_heap: 
            src_time, src_node = heapq.heappop(min_heap) 
            
            if src_node in shortest_map: 
                continue

            shortest_map[src_node] = src_time

            for dst_node, dst_time in adj_list[src_node]:
                if dst_node not in shortest_map: 
                    heapq.heappush(min_heap, (dst_time + src_time, dst_node))
        
        return -1 if len(shortest_map) != n else max(shortest_map.values())
