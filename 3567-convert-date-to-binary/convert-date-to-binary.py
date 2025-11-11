class Solution:
    def decimaltobinary(self, n: int) -> str:
        if n == 0:
            return "0"
        res = ""
        while n > 0:
            res += str(n % 2)
            n //= 2
        return res[::-1] 

    def convertDateToBinary(self, date: str) -> str:
        y = self.decimaltobinary(int(date[:4]))
        m = self.decimaltobinary(int(date[5:7]))
        d = self.decimaltobinary(int(date[8:]))
        return f"{y}-{m}-{d}"