class Solution:
    def __init__(self):
        self.result = []
        self.subtrees = {}

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.dfs(root)
        return self.result
    
    def dfs(self, root: TreeNode) -> str:
        if not root:
            return "#"

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        subtree = ",".join([left, right, str(root.val)])
        self.subtrees[subtree] = self.subtrees.get(subtree, 0) + 1
        if self.subtrees[subtree] == 2:
            self.result.append(root)

        return subtree