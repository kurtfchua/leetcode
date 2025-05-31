class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            count = dfs(i+1)
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
                    count += dfs(i+2)
            
            return count 
        #return dfs(0)
        mem = {}
        def top_down(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0 
            if i in mem: 
                return mem[i]
            
            count = top_down(i+1)
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
                    count += top_down(i+2)
            mem[i] = count
            
            return mem[i]

        return top_down(0)
        