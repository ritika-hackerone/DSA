# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TC: O(n)   SC: O(1)
        # Using slow and fast ptr : Find the middle using slow/fast pointers, reverse the second half, then compare both halves node by node. If all values match, the linked list is a palindrome.
        slow = fast = head

        # find middle  
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  
        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True    