class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep a hashmap to store the sorted values of strs as keys
        # if sorted value is in the hashmap we append the unsorted value
        # if not we initiate the value with this unsorted string
        # we then iterate through all the values and append them to a list and return
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        
        res = []
        for v in anagrams.values():
            res.append(v)
        
        return res

        