# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return

        dummy = ListNode(0)
        tail = dummy
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            _, i, min_node = heapq.heappop(heap)
            tail.next = min_node
            tail = tail.next
            
            if min_node.next:
                next_node = min_node.next
                heapq.heappush(heap, (next_node.val, i, next_node))
        
        head = dummy.next
        return head
        