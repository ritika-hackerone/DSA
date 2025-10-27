class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')

        for current in nums:
            if current > max1:
                max3 = max2
                max2 = max1
                max1 = current
            elif current < max1 and current > max2:
                max3 = max2
                max2 = current 
            elif current < max2 and current > max3:
                max3 = current

        if max3 == float('-inf'):
            return max1
        else:
            return max3
        