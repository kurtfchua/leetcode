class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # have 2 pointers pointing to the start and end of nums list
        # create a list of length nums consisting only of zeros
        # compare the 2 locations of the list, whicever is greater we add to the result list
        # increment and decrement based on which number was chosen
        result = [0 for x in range(len(nums))]
        left, right = 0 , len(nums) - 1
        i = len(result) - 1

        while left <= right: 
            left_squared = nums[left] * nums[left]
            right_squared = nums[right] * nums[right]
            
            if left_squared >= right_squared: 
                result[i] = left_squared
                left += 1
            if right_squared > left_squared:
                result[i] = right_squared
                right -= 1
            i -= 1

        return result 

        # T O(n): we must iterate through all of nums to build the new list
        # S O(n): we create a new list that is the same size as nums