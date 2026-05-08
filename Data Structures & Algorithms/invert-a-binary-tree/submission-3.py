# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 使用queue
        # 要處理的放進queue
        # root放進queue
        # 從queue拿出來node
        # 取得queue的children放入queue，
        # children invert對調
        # 重複:從queue拿出來node
        if not root:
            return root
        q = deque()
        q.append(root)
        # print(q)
        while q:
            node = q.popleft()
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            node.left, node.right = node.right, node.left

        return root