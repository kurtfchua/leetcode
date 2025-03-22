class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # iterate nums using 2 pointer technique, left and right
        # right will update whenever the next elem is different from the last 
        # right will update whenever the next elem is the same as well
        # left will only update whenever the first condition is met
        # we then update nums[left] -> nums[right] when we find the next unqiue element
        # left will have the amount of unqiue elements there are

        left = right = 1

        while right < len(nums):
            if nums[right-1] != nums[right]:
                nums[left] = nums[right]
                left+=1
                right+=1
            else:
                right+=1
        
        return left



        