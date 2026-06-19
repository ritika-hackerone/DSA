class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        ans = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                length = right - left + 1
                ans = min(ans, length)
                total -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans
        