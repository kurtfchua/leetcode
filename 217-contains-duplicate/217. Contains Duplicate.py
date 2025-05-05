class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)

        return False

        # S O(n) - we pass through nums once and add to the set
        # T O(n) - we create a set that grows linearly with nums
        