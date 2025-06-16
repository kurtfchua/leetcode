class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)

        max_idx = 0
        res = 0
        for k, v in freq.items():
            if v > max_idx:
                res = k
                max_idx = v
        
        return res 



        