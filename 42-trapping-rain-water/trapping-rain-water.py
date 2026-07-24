class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        answer = 0
        maxLeft , maxRight = height[0] , height[n-1]
        left , right = 1 , n-2
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    answer += maxLeft - height[left]
                    left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    answer += maxRight - height[right]
                    right -= 1
        return answer