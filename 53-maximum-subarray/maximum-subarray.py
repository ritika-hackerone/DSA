class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Uses Kadane's Algo
        res = nums[0] # maximum total so far
        total = 0     # keeps track of subarray, reset negative value of 'total' --> 0
        for n in nums:
            if total < 0:
                total = 0
            total += n
            res = max(res, total)
        return res
                
