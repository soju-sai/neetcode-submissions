# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        history = set()
        while head.next:
            if head.val in history:
                return True
            history.add(head.val)
            head = head.next
        return False