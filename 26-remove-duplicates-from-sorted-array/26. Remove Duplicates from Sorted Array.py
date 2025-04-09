class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # iterate through the array using 2 pointers i and j 
        # i will hold the next elem that needs to be swapped
        # j will hold the next unique eleme found
        # we swap arr[i] and arr[j] when arr[j] != arr[j-1], unique elem found
        # then increment i and j to perform next swap
        # otherwise we increment j to find next unique element
        # i is therefore boundary of the sorted array, return i to get the amount
       
        # we start at 1, first elem is already sorted
        i = j = 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i +=1
                j +=1
            else:
                j +=1
        
        return i 
    


        