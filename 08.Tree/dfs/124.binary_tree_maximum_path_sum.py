class Solution:
    def __init__(self):
        self.max_val = float("-inf")
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_val
    
    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_val = self.dfs(root.left)
        right_val = self.dfs(root.right)

        self.max_val = max(self.max_val, left_val + right_val + root.val)
        
        return max(0, root.val + max(left_val, right_val)) # 通过根节点的单边最大值