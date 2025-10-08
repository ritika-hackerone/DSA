# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # T.C --> O(n) , S.C --> O(log n)

        def hgtBalancedBST(l, r):

            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = hgtBalancedBST(l, mid - 1)
            root.right = hgtBalancedBST(mid + 1, r)
            return root

        return hgtBalancedBST(0, len(nums) - 1)
            