class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # iterate nums using 2 pointers, left and right
        # right pointer will keep track of elements != val
        # it will update in the either case 
        # in the case that elem != val, nums[left] = nums[right]
        # then we update left accordingly by 1

        left = right = 0

        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left +=1
                right+=1
            else:
                right+=1
        
        return left 