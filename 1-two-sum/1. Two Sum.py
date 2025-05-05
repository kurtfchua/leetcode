class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}

        for i in range(len(nums)):
            if nums[i] in comps:
                return [i, comps[nums[i]]]
            else:
                comps[target-nums[i]] = i
        
        # T O(n) - we must iterate through nums to find the 2 pairs and build comps hashmap
        # S O(n) - the hashmap grows with our nums list