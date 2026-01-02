class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = min(height[left], height[right]) * (right - left)
        max_height = max(height)

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > result:
                result = area
            if result > max_height * (right - left):
                return result

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return result