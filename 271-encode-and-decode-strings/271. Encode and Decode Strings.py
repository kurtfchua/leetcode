class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # for each string add chr(24) at end
        # append each new string to last string
        encoded_string = ""
        for word in strs:
            word+= chr(24)
            encoded_string+=word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # split string by delimiter chr(24)
        decoded_string = s.split(chr(24))
        if not decoded_string[-1]:
            decoded_string.pop()
        return decoded_string


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))