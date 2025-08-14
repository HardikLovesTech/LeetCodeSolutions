class Solution:
    def largestGoodInteger(self, num: str) -> str:
        j , k = 0
        sortedArr = ""
        for i in num:
            if(i <= len(num) - 2):
                j = i + 1
                k = i + 2
                if(num[i] == num[j] == num[k]):
                    sortedArr.append(num[i] + num[j] + num[k])

        return sortedArr