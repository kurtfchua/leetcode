class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers i, j starting from 0..end of list
        # if sum == target return [i,j]
        # if sum < target, increment i 
        # if sum > target, decrement j
        i, j = 0, len(numbers) - 1

        while i < j: 
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            if sum < target: 
                i += 1
            if sum > target: 
                j -= 1
        
    
        