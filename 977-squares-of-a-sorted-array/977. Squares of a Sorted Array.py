class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            square = nums[i] * nums[i]
            nums[i] = square
        return sorted(nums)
        