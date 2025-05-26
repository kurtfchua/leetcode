class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(nums):
            if len(nums) == 0: return [[]]

            permutations = self.permute(nums[1:])
            res = []

            for perm in permutations:
                for i in range(len(perm)+1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, nums[0])
                    res.append(perm_copy)

            return res 
            
        self.res = []
        def backtrack(nums, idx): 
            if idx == len(nums):
                self.res.append(nums.copy())
                return 
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(nums, idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        backtrack(nums, 0)

        return self.res

