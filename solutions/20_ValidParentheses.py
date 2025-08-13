class Solution:
    def isValid(self, s: str) -> bool:
        parenthisis = []
        map = { ')' : '(' , ']' : '[' , '}' : '{'}
        for char in s:
            if char in map:
                top =   parenthisis.pop() if parenthisis else '#'
                if map[char] != top:
                    return False
            else:
                parenthisis.append(char)
        return not parenthisis