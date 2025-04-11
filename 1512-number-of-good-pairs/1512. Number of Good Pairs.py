class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # iterate through nums and for each num iterate through list to find match of num
        # if match exists increment count 
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    count+=1
        
        return count

        