# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 先做出queue實現BFS, None的node直接給"N"
        queue = deque([])
        result = []
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        des = data.split(",")
        if des[0] == "N":
            return None
        ind = 0
        queue = deque([])
        root = TreeNode(des[ind])
        queue.append(root)
        ind += 1
        while queue:
            node = queue.popleft()
            if des[ind] != "N":
                node.left = TreeNode(des[ind])
                queue.append(node.left)
            ind += 1
            if des[ind] != "N":
                node.right = TreeNode(des[ind])
                queue.append(node.right)
            ind += 1
            # if des[ind] == "N":
            #     ind += 1
        return root

