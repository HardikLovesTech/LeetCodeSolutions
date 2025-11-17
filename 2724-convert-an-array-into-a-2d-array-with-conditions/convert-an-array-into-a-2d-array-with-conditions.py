class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count=0
        res=[]
        mark=[False]*len(nums)
        while len(nums)!=count:
            output=[]
            for i in range(len(nums)):
                if nums[i] not in output and mark[i]==False:
                    output.append(nums[i])
                    mark[i]=True
                    count+=1
            res.append(output)
        return res
