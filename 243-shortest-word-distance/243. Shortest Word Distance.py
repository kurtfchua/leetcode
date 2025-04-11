class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # set two indexes to -1, to say we haven't found them yet
        # set min_diff to be infinite
        # iterate through wordsDict and update the indexes whenever we find word1 and word2
        # when indexes aren't -1 we set min_diff to be the smaller between min_diff and new diff
        # constantly calculate the min_diff and compare while indexes for the words change
        # return min_diff
        index1 = index2 = -1
        min_diff = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            if wordsDict[i] == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                min_diff = min(min_diff, abs(index2-index1))

        return min_diff

        # T O(n): we must iterate through list to find all instances of word1 and word2
        # S O(1): done in-place, no new data structures were used


        