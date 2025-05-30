class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList: 
            return 0 
        
        adj_list = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList: 
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                adj_list[key].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])

        length = 1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == endWord: 
                    return length
                for i in range(len(word)):
                    key = node[:i] + "*" + node[i+1:]
                    for neighbor in adj_list[key]:
                        if neighbor not in visited: 
                            queue.append(neighbor)
                            visited.add(neighbor)
            length += 1

        return 0        