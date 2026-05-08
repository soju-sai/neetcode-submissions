# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None
            return
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy.next
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next

        # # 找到中點     
        # slow, fast, index = head, head.next, 0
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     index += 1
        
        # length = (index+1) * 2
        # print(length)
        # targetIndex = length - n
        # print(targetIndex)
        # current, index = head, 0
        # while current:
        #     if index == targetIndex:
        #         tmp = current.next
        #         current.next = tmp.next
        #         tmp = None
        #     current = current.next
        #     index += 1
        

