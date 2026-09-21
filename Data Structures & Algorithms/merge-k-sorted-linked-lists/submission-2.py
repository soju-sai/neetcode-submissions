# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        bucket = defaultdict(int)
        for l in lists:
            while l:
                bucket[l.val] += 1
                l = l.next
        
        print(bucket)
        bu = sorted(bucket.items())

        dummy = ListNode(0)
        head = dummy
        for item in bu:
            count = item[1]
            while count > 0:
                head.next = ListNode(item[0])
                head = head.next
                count -= 1
        
        return dummy.next
        