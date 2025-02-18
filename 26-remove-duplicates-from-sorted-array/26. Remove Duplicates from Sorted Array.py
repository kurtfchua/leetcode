class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # iterate through nums with left, right pointers
        # left will be the most recent unique value we have found
        # right will be the value to find the next unique when incrementing
        # if nums[right] != nums[right -1] we have found the next unique value
        # then we reassign nums[left] to the nums[right] to replace this value with the most updated unique value
        # otherwise its a repeated elem and we must increment right by 1 to find the next unique value
        left = right = 1

        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left+=1
                right+=1
            else:
                right+=1
            
        return left

        