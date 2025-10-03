class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        # initialize 2 ptrs(left and right) with starting and ending indices
        lt = 0
        rt = len(nums) - 1

        while(lt <= rt):
             mid = (lt + rt) // 2
             
             if nums[mid] == target:
                return mid
             elif nums[mid] > target:
                rt = mid - 1
             else:
                lt = mid + 1

        return lt

            
