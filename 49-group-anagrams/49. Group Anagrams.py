class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs: 
            char_count = [0] * 26 
            for c in word: 
                char_count[ord(c)-ord('a')] += 1
            hashmap[tuple(char_count)].append(word)

        return list(hashmap.values())
