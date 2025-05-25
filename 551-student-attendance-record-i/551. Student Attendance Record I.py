class Solution:
    def checkRecord(self, s: str) -> bool:
        record_counts = Counter(s)

        if record_counts['A'] >= 2: return False
        if 'LLL' in s: return False
        
        return True


