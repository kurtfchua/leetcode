class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            groups[''.join(sorted_word)].append(word)

        return list(groups.values())


        