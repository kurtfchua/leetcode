class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False

        def dfs(i, target):
            if i == len(nums):
                return target == 0
            if target < 0: 
                return False
            
            return dfs(i+1, target) or dfs(i+1, target-nums[i])
        
        #return dfs(0, sum(nums)//2)
        mem = {}
        def top_down(i, target):
            if i == len(nums):
                return target == 0
            if target < 0: 
                return False
            if (i, target) in mem: 
                return mem[(i, target)]
            
            exclude = top_down(i+1, target) 
            include = top_down(i+1, target-nums[i])
            mem[(i, target)] = exclude or include

            return mem[(i, target)]
        
        #return top_down(0, sum(nums)//2)
        
        def bottom_up(target):
            dp = set()
            dp.add(0)

            for i in range(len(nums)-1,-1,-1):
                next_dp = set()
                for t in dp:
                    if t + nums[i] == target: 
                        return True
                    next_dp.add(t)
                    next_dp.add(t+nums[i])
                dp = next_dp

            return target in dp

        return bottom_up(sum(nums) // 2) 
