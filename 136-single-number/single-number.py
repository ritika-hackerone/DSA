class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bitwise XOR
        result = 0

        for n in nums:
            result ^= n

        return result


