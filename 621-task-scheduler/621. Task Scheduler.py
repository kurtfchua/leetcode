class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        hashmap = Counter(tasks)
        heap = [-value for value in hashmap.values()]
        heapq.heapify(heap)


        queue = deque()
        time = 0

        while heap or queue: 
            time += 1

            if heap: 
                count = heapq.heappop(heap) + 1
                if count: 
                    queue.append((count, time + n))
            else:
                time = queue[0][1]
            
            if queue and queue[0][1] == time: 
                heapq.heappush(heap, queue.popleft()[0])
        
        return time