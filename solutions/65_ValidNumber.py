class Solution:
    def isNumber(self, s: str) -> bool:
        string = "1234567890-+eE."
        s1 = set(s)
        if s[0] != 'e' or s[0] != '.':
            return False
        else:
            for ch in s1:
                if ch in string:
                    return True
            return False