class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Minimum is in right half
            if nums[mid] > nums[high]:
                low = mid + 1

            # Minimum is in left half including mid
            elif nums[mid] < nums[high]:
                high = mid

            # Duplicate case
            else:
                high -= 1

        return nums[low]