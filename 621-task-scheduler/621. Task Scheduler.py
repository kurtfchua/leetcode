class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        heap = [-val for val in task_freq.values()]
        heapq.heapify(heap)

        queue = deque()
        time = 0

        while heap or queue: 
            time += 1
            if heap: 
                count = 1 + heapq.heappop(heap)
                if count: 
                    queue.append((count, time + n))
            else: 
                time = queue[0][1]

            if queue and queue[0][1] == time: 
                heapq.heappush(heap, queue.popleft()[0]) 

        return time       