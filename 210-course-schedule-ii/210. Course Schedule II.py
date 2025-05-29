class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        processed, cycle = set(), set()
        path = []

        def dfs(course):
            if course in cycle: 
                return False
            if course in processed: 
                return True
            
            cycle.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(course)
            processed.add(course)
            path.append(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return path
        