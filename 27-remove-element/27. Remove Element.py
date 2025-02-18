class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # implement two pointer technique i, j being slow and fast pointers
        # if j != val we swap nums[i] and nums[j] and increment both
        # otherwise we increment j to find the next elem != val
        # resulting list will swap all elems != val to the first k elements
        # i will hold the amount of times we've swaped 
        i = j = 0
        
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
                j+=1
            else:
                j+=1
        
        return i