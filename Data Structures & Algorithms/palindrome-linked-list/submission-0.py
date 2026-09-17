# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # by stack
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        while head:
            if head.val != stack.pop():
                return False
            head = head.next
        
        return True


    # time: O(2n), space: O(2n)
    def isPalindrome_v1(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        return arr == arr[::-1]