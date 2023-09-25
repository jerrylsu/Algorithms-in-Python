class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traverse(nums)
    
    def traverse(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_val = max(nums)
        index = nums.index(max_val)
        root = TreeNode(max_val)
        
        root.left = self.traverse(nums[:index])
        root.right = self.traverse(nums[index + 1:])  # list切片越界为[]
        
        return root
