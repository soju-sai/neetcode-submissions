# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = head
        while curr:
            if curr.next == slow:
                curr.next = None
            curr = curr.next

        prev, curr = None, slow
        while curr:
            af = curr.next
            curr.next = prev
            prev = curr
            curr = af
        
        middle = prev
        dummy = ListNode(0, head)
        curr = head

        while curr and middle:
            tmp = curr.next if curr.next else middle.next
            curr.next = middle
            curr = curr.next
            middle = middle.next
            curr.next = tmp
            curr = curr.next

        
        
