# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 知道preorder的順序：根 左 右，inorder的順序：左 根 右
    # 以preorder按順序移動取得root，找出inorder[preorder root]的位置取得左右子樹的區間
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建立inorder的hashmap幫助快速找到index
        inorderPosition = {val: ind for ind, val in enumerate(inorder)}
        # 預設preorder用的移動指標
        self.preIndex = 0

        def dfs(l, r):
            # 記得設定base case避免out of range
            if l > r:
                return None
            # 取得root的值
            rootVal = preorder[self.preIndex]
            # 取得root在inorder的位置
            mid = inorderPosition[rootVal]
            # 取好了之後移動指標可以前進一格
            self.preIndex += 1
            # 做出TreeNode本身
            root = TreeNode(rootVal)
            # 遞迴做出左右子樹
            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)
            # 最後記得回傳根本身
            return root

        # 傳入要組成Binary Tree的區間
        return dfs(0, len(inorder)-1)
        

    def buildTree_v2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: ind for ind, val in enumerate(inorder)} # 先做出可以快速找到root index的inorder對照表
        self.preIndex = 0

        def dfs(l, r):
            if l > r:
                return None
            # 先做好root
            root_val = preorder[self.preIndex]
            self.preIndex += 1
            mid = indices[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l, mid-1) # 重點[1]
            root.right = dfs(mid+1, r) # 重點[2]
            return root
        
        return dfs(0, len(inorder)-1)

    def buildTree_v1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder的前頭一定是root
        # 而inorder在preorder取得root後，左側的是left tree，右側的是right tree
        # 每次都把整個left和right tree的array區間當引數下傳；反覆下去，最後拼出所有的tree全貌
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root