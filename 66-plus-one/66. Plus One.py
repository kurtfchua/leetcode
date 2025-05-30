class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ""
        for num in digits: 
            digit += str(num)

        digit = int(digit) + 1
        digit = str(digit)
        res = [int(c) for c in digit]

        return res
    
        