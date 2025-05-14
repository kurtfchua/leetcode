class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_pos = set()

        for num in nums:
            if num > 0:
                unique_pos.add(num)
        
        return len(unique_pos)
        