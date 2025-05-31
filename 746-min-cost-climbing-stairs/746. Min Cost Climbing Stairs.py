class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def basic(i):
            if i >= len(cost):
                return 0 
            
            return cost[i] + min(basic(i+1), basic(i+2))
        
        mem = {}
        def top_down(i):
            if i >= len(cost):
                return 0 
            if i in mem: 
                return mem[i]
            
            mem[i] = cost[i] + (min(top_down(i+1), top_down(i+2)))

            return mem[i]
        
        def bottom_up(i):
            a, b = 0, 0
            
            for i in range(len(cost)-1, -1, -1):
                a, b = b, cost[i] + min(a, b)

            return min(a,b)
        
        def bottom_up_2():
            cost.append(0)
            for i in range(len(cost)-3, -1, -1):
                cost[i] += min(cost[i+1], cost[i+2])
            
            return min(cost[0], cost[1])

        return bottom_up_2()

        #return min(top_down(0), top_down(1))

        #return min(basic(0), basic(1))


        