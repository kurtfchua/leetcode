class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            counts = [0]*26
            for c in word:
                counts[ord(c)-ord('a')] += 1
            hashmap[tuple(counts)].append(word)
        
        return list(hashmap.values())
        