class Solution:
    def reverseVowels(self, s: str) -> str:
        # use two pointers i, j at the start and end of list respectively
        # if i and j are both vowels swap
        # otherwise increment and decrement pointers as needed
        # continue until we reach middle of the list 

        i, j = 0, len(s) - 1
        vowel = 'aeiouAEIOU'
        s = list(s)
        
        while i < j:
            if s[i] in vowel and s[j] in vowel:
                temp = s[j]
                s[j] = s[i]
                s[i] = temp
                i += 1
                j -= 1
            if s[i] not in vowel:
                i += 1
            if s[j] not in vowel:
                j -= 1

        return "".join(s)
        