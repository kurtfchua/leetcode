class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # iterate with 2 pointers i, j 
        # i will be the next element to be removed
        # j will be the next element != val
        # if j != val swap i with j, then increment i and j 
        # otherwise increment j 

        i = j = 0 

        while j < len(nums):
            if nums[j] != val: 
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j+=1
        
        return i
        