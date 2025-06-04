class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # for every word append #len(word)word to result string
        res = ""
        for word in strs: 
            res += str(len(word)) +"#" +  word

        return res
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # iterate through word, find index of # get length the next index, slice string from number to len(word) update i
        res = []
        i = j = 0
        while i < len(s):
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1:j+length+1] 
            res.append(word)
            i = j+length+1
            j = i 

        return res       


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))