class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left , right = 0 , len(height)-1
        LeftMax , RightMax = 0 , 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= LeftMax:
                    LeftMax = height[left]
                else:
                    res += LeftMax - height[left]
                left += 1
            else:
                if height[right] >= RightMax:
                    RightMax = height[right]
                else:
                    res += RightMax - height[right]
                right -= 1
        return res