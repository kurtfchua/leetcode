class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use 2 pointers i, j at the start and end of the list
        # at i and j we check if theyre alphanumeric
        # if not, we ignore and increment and decrement respectively
        # if alphanumeric, check if i and j are equal 
        # if equal proceed to increment and decrement both pointers
        # otherwise immediately return false 
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True 

        # T O(n): we iterate through all the elements in the string
        # S O(1): we check string in place, no new data structures were used

                       