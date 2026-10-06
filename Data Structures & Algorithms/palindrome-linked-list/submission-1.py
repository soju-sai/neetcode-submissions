# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # compare with reversed linked list
        shallow = deepcopy(head)
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        while prev:
            print(prev.val, shallow.val)
            if prev.val != shallow.val:
                return False
            prev = prev.next
            shallow = shallow.next

        if shallow:
            return False

        return True