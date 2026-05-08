# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 重點：BST就是左小右大，且所有的子孫也必須比parent大或小才算數
        def isValid(node, left, right):
            if not node:
                return True
            # 確認值在left和right的範圍內，否則回傳false
            if not (node.val > left and node.val < right):
                return False

            # 確認children的node也小或大於parent
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        return isValid(root, float("-inf"), float("inf"))


    def isValidBST_v1(self, root: Optional[TreeNode]) -> bool:
        # 這個做法只能確認一層node底下的children
        # 左tree val一定小於root val, 右tree則相反
        # 感覺要用recursion反覆確認，有不符條件的就return false
        #   base case: 不符條件 false, 不存在 node return none
        if not root:
            return False

        node = root

        if node.left:
            if node.left.val >= node.val:
                return False
        if node.right:
            if node.right.val <= node.val:
                return False

        leftRes = self.isValid(node.left)
        rightRes = self.isValid(node.right)

        print(leftRes, rightRes)
        if leftRes and rightRes:
            return True
        else:
            return False

    def isValid_v1(self, node):
        if not node:
            return True
        
        if node.left:
            if node.left.val >= node.val:
                return False
        if node.right:
            if node.right.val <= node.val:
                return False
        
        return self.isValid(node.left) and self.isValid(node.right)
