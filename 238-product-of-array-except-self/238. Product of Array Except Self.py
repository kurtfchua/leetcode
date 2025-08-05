class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        prefix = 1

        for num in nums:
            prefix_prod.append(prefix)
            prefix *= num
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            prefix_prod[i] *= suffix 
            suffix *= nums[i]
        
        return prefix_prod