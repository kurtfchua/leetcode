class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # pointers i, j will point to next to be replaced and next unqiue element
        i = j = 1

        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i+=1
            j+=1
        
        return i
        
        