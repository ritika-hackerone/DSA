class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product =  min_product = result = nums[0]
        for n in nums[1:]:
            if n < 0:
                max_product, min_product = min_product, max_product
            max_product = max(n, max_product * n)
            min_product = min(n, min_product * n)
            result = max(result , max_product)
        return result
       
    

        