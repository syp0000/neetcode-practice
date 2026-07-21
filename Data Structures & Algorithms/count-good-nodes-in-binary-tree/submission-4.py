# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        result = []
        queue = deque([(root, root.val)])
        ans = []

        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                ans.append(node.val)
            new_max = max(max_val, node.val)
            
            if node.left: queue.append((node.left,new_max))
            if node.right: queue.append((node.right,new_max))
        return len(ans)


        