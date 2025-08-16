import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 :
            return int(((math.log(n))/(math.log(4)))) == ((math.log(n))/(math.log(4)))
        else:
            return False