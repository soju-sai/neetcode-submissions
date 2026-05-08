# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 找出中點，以中點將ll分爲前後兩段
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 將後段ll反轉
        # secondLL = slow.next
        # theLastNode = fast
        secCurr = slow.next
        secPrev = None
        slow.next = None
        while secCurr:
            temp = secCurr.next
            secCurr.next = secPrev
            secPrev = secCurr
            secCurr = temp

        # 將兩段交叉排列
        first, second = head, secPrev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        # current = head
        # while current:
        #     print(current.val)
        #     current = current.next
        
                
        # nodeList = []
        # index = 0
        # while head:
        #     nodeList.append(head)
        #     head = head.next

        # count = 1
        # queueList = deque()
        # while count <= len(nodeList):
        #     if count % 2 == 1:
        #         queueList.append(nodeList[count - 1])
        #     else:
        #         queueList.append(nodeList[len(nodeList) - 1])
        #     count += 1
        
        # while queueList:
        #     print(queueList.popleft().val)
