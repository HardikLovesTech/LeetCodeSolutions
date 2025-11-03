class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original=x
        sum=0
        while x>0:
            sum+=x%10
            x=x//10
        if sum!=0 and original%sum == 0:
            return sum
        else:
            return -1
        