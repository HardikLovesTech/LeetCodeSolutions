class Solution:
    def maximum69Number(self, num: int) -> int:
        NumList = list(str(num))
        
        for i in range(len(NumList)):
            if NumList[i] == '6':
                NumList[i] = '9'
                break  
        
        return int("".join(NumList))
