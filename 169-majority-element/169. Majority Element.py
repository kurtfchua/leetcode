class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        freq = Counter(nums)

        for k, v in freq.items():
            if v > n:
                return k 
        

        
        