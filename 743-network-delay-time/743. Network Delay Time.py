class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for src, dst, time in times: 
            adj_list[src].append((dst, time))
        
        shortest = {}
        min_heap = [(0, k)]

        while min_heap: 
            time1, node1 = heapq.heappop(min_heap)
            if node1 in shortest:
                continue
            
            shortest[node1] = time1

            for node2, time2 in adj_list[node1]:
                if node2 not in shortest:
                    heapq.heappush(min_heap, (time2+time1, node2))

        return -1 if len(shortest) != n else max(shortest.values())        