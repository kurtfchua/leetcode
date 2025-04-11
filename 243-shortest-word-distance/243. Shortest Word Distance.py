class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # if we find word1 or word 2 in list first, find the other word and calc diff
        # update diff if smaller than current diff
        # return diff
        i = 0 
        min_diff = float('inf')

        while i < len(wordsDict):
            if wordsDict[i] == word1: 
                for j in range(i +1, len(wordsDict)):
                    if wordsDict[j] == word2:
                        if min_diff != 0 and abs(j-i) < min_diff:
                            min_diff = abs(j-i)
            if wordsDict[i] == word2: 
                for j in range(i +1, len(wordsDict)):
                    if wordsDict[j] == word1:
                        if min_diff != 0 and abs(j-i) < min_diff:
                            min_diff = abs(j-i)
            i += 1
        return min_diff

        