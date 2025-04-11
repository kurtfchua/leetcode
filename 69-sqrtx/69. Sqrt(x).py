class Solution:
    def mySqrt(self, x: int) -> int:
        # 2 pointers i, j that are 1..x
        # while i < j: we keep updating i and j until we find i * j  = x
        # if product < x. increment i if product > x decrement j
        # repeat until i = j
        if x < 2: 
            return x

        i, j = 1, x 
        sqrt = 1

        while i <= j: 
            middle = (i+j) // 2
            if middle * middle == x: 
                return middle
            if middle * middle < x:
                sqrt = middle
                i  = middle + 1
            if middle * middle > x: 
                j = middle -1
      
        return sqrt

        