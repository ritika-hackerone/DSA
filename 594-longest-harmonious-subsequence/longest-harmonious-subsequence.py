class Solution:
    def findLHS(self, nums: List[int]) -> int:
        occurence = defaultdict(int)
        res = 0
        for num in nums:
            occurence[num] += 1

        for num in occurence:
            if num + 1 in occurence:
                res = max(res, occurence[num] + occurence[num + 1])
        
        return res


        