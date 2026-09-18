# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        cm, cn = m, n
        while curr:
            if cm == 1:
                while curr.next and cn > 0:
                    curr.next = curr.next.next
                    cn -= 1
                cm, cn = m, n
            else:
                cm -= 1
            curr = curr.next
        
        return dummy.next
