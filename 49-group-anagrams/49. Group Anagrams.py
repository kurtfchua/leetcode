class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            groups[tuple(sorted(word))].append(word)
        
        return list(groups.values())
                
