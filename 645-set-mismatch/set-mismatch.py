class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Return [duplicate, missing]
        actual_sum = 0
        n = len(nums)
        check_duplicate = set()
        
        for num in nums:
            actual_sum = actual_sum + num
            if num in check_duplicate:
                duplicate = num
            else:
                check_duplicate.add(num)

        expected_sum = (n*(n+1))//2
        missing = expected_sum - (actual_sum - duplicate)
        return [duplicate, missing]


        