class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through nums, and calculate the diff between target and nums[i]
        # we will use the diff as the key for the diff of this current index and target and the value as the index it was found in
        # if a nums[i] is equal to the diff found earlier in the array, return the value of this diff in the dictionary + the current index where we found it
        diff_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_map:
                return [i, diff_map[diff]]
            else:
                diff_map[nums[i]] = i 