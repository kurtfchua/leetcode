class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a hashmap to store all anagrams as values
        # tuple from 0..25 will hold counts of each char in word
        # return values of hashmap as a list
        anagrams = defaultdict(list)
        for word in strs: 
            count = [0] * 26
            for c in word: 
                count[ord(c)-ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())

        # T O(m*n) - we iterate through every word in the list and then every char in each word. m being the length of the list and n being the average length of each word
        # S O(m*n) - we create a hashmap that grows linearly with the word list. each word is on average n length.
        