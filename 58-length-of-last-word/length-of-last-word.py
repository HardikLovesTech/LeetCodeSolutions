class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = s.strip().split()
        return len(length[-1]) if length else 0