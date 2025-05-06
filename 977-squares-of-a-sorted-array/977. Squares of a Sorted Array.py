class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i, j = 0, n - 1
        for k in range(len(nums)-1,-1,-1):
            i_squared = nums[i] * nums[i]
            j_squared = nums[j] * nums[j]
            if i_squared >= j_squared:
                res[k] = i_squared
                i +=1
            else:
                res[k] = j_squared
                j-=1
        
        return res


        