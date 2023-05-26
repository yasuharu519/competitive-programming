# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque()
        queue.append((root, None, 0))
        current_level = 0

        while queue:
            level_layer = []
            current_level_sum = 0
            while queue and queue[0][2] == current_level:
                q = queue.popleft()
                current_level_sum += q[0].val
                level_layer.append(q)

            prevProcessedNodeInfo = None
            for node, parent, _ in level_layer:
                sameparent_sum = 0
                if prevProcessedNodeInfo and prevProcessedNodeInfo[1] == parent:
                    sameparent_sum = prevProcessedNodeInfo[0] + node.val
                else:
                    if parent:
                        if parent.left:
                            sameparent_sum += parent.left.val
                        if parent.right:
                            sameparent_sum += parent.right.val
                    else:
                        sameparent_sum = node.val
                prevProcessedNodeInfo = (node.val, parent)
                node.val = current_level_sum - sameparent_sum

                if node.left:
                    queue.append((node.left, node, current_level + 1))
                if node.right:
                    queue.append((node.right, node, current_level + 1))
            current_level += 1

        return root
