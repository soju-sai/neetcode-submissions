# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p和q同時用BFS
        # 每走一步，確認一次p和q的node.val是否相同
        # 不同就直接return False
        # 直到整個p跑完，回傳True
        # p或q其中一個空了，另一個還沒也是False
        pq, qq = deque(), deque()
        pq.append(p)
        qq.append(q)

        while pq and qq:
            pqNode = pq.popleft()
            qqNode = qq.popleft()
            if pqNode and qqNode:
                if pqNode.val != qqNode.val:
                    return False
            elif not pqNode and qqNode:
                return False
            elif pqNode and not qqNode:
                return False
            
            if pqNode:
                pq.append(pqNode.left)
                pq.append(pqNode.right)
            if qqNode:
                qq.append(qqNode.left)
                qq.append(qqNode.right)
            # else:
            #     qq.append(None)
        
        if len(pq) != len(qq):
            return False

        return True