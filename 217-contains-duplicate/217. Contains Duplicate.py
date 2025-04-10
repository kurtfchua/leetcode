class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # iterate through nums and add num to set if num is not in set
        # otherwise return True
        # if we iterate through entire list without duplicates return False

        dup_set = set()

        for num in nums:
            if num in dup_set:
                return True
            else:
                dup_set.add(num)
        
        return False

        # T O(n): we have to iterate through entire nums to find duplicates
        # S O(n): we create a new set of size O(n)
        