class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1   # 通过根节点的最大深度
        