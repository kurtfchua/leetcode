class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def find_pref_suff(nums):
            prefix = suffix = 0
            n, res = len(nums), nums[0]

            for i in range(n):
                prefix = nums[i] * (prefix or 1)
                suffix = nums[n-1-i] * (suffix or 1)
                res = max(res, max(prefix, suffix))

            return res
        
        def dp(nums):
            curr_max, curr_min = 1, 1
            max_prod = nums[0]

            for num in nums:
                tmp = curr_max * num
                curr_max = max(num*curr_max, num*curr_min, num)
                curr_min = min(tmp, num*curr_min, num) 
                max_prod = max(max_prod, curr_max)
            
            return max_prod
            
        return dp(nums)