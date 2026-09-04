from heapq import heappush, heappop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def dfs(root, heap):
            # nonlocal heap, k
            if not root:
                return None
            

            diff = abs(target - root.val)
            if len(heap) < k:
                heappush(heap, (-diff, root.val))
                # heappush(heap, (-diff, root.val)) # 因為 heap 只能從最小排出，所以加負號把最大的顛倒放在前面，方便排出
            else:
                if -diff > heap[0][0]: # 如果目前的距離比最外面的heap還要近，把最外面拿出來，目前值放進去
                    heappop(heap)
                    heappush(heap, (-diff, root.val))

            dfs(root.left, heap)
            dfs(root.right, heap)

        heap = []
        dfs(root, heap)
        
        return [val for diff, val in heap]