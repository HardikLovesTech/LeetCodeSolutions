class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        MaxWater = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            MaxWater = max(MaxWater, w * h)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  
        return MaxWater
