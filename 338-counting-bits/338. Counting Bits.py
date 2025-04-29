class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        res = []
        while i <= n:
            j = i 
            count = 0
            while j > 0:
                if j & 1:
                    count += 1
                j = j >> 1
            i += 1
            res.append(count)
        return res

            



        