# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 要用DFS(stack)遍歷root，找subRoot的頭
        # 沒找到subRoot頭就直接return False
        # 從找到subRoot的頭開始，放棄本來Root的其他部分，用same tree的方式比較


        def isSame(r, s):
            # 如果r和s都是None就是true
            # 如果r和s都有值且val相同，重複確認left和right
            # 其他情況return False
            if not r and not s:
                return True
            elif r and s and r.val == s.val:
                print(r.val, s.val)
                return isSame(r.left, s.left) and isSame(r.right, s.right)
            else:
                print(r, s)
                print('it is false')
                return False
        
        # ----- start -----
        stack = [root]
        # node = stack.pop()
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    # stack = [node]
                    # break
                    if isSame(node, subRoot):
                        return True
                print(node.val)
                stack.append(node.right)
                stack.append(node.left)
        if len(stack) == 0:
            return False
        node = stack.pop()
        print(node.val)
        return False

        # return isSame(node, subRoot)
        
