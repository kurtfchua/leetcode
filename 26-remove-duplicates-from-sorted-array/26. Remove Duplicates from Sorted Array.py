class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # have 2 pointers left and right
        # with pointers iterate through nums
        # left and right will increment if the next number is different from both
        # otherwise if its a repeated number we increment right only
        # so left will hold the most updated unique value and right will find the next unique number
        # we then return left at the end since the amount of increments will be the amount of times we find a unique number

        # we start at index 1 becaue the first element will always be the first unique number
        left = 1
        right = 1

        while right < len(nums):
            # check if next elem is equal to curr elem
            if nums[right] != nums[right-1]:
                # update both left and right ++1
                nums[left] = nums[right]
                left +=1
                right +=1
            else:
                # find next unique elem
                right+= 1
        # left will hold the number of unique elems we found in nums
        return left
        