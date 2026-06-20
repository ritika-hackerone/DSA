class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = len(nums)
        res = []
        for i in range(s):
            n = nums[i] ** 2
            res.append(n)
        return sorted(res)


        