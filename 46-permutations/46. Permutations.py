class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(nums):
            if len(nums) == 0: return [[]]

            permutations = self.permute(nums[1:])
            res = []

            for perm in permutations:
                for i in range(len(perm)+1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, nums[0])
                    res.append(perm_copy)

            return res 

        return recur(nums)       