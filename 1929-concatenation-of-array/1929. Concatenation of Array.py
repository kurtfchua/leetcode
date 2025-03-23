class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Approach 1: return nums + nums
        # Approach 2: loop through nums twice and append elements to a new array and return it
        
        # Approach 1
        # new_array = []

        # for i in range(2):
        #     for num in nums: 
        #         new_array.append(num)

        # return new_array

        # Approach 2
        return nums + nums

        # Space Complexity: O(n)
        # TIme Complexity: O(n)