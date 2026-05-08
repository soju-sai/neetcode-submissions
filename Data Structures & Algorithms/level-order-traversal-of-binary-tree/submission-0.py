# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 重點是怎麼判斷是同樣level
        # 先試著寫一個BFS的traversal
        # 每層跑for迴圈，把當層q清空且加入結果，同時加入children到新一層的queue
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res