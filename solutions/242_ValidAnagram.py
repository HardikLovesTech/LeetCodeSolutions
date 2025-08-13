class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s.lower())
        t1 = list(t.lower())
        s1.sort()
        t1.sort()
        return s1 == t1

