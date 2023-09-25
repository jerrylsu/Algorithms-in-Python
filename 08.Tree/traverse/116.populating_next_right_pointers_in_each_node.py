"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.traverse(root.left, root.right)
        return root
    
    def traverse(self, left, right):
        if not left or not right:
            return
        left.next = right
        self.traverse(left.left, left.right)
        self.traverse(left.right, right.left)
        self.traverse(right.left, right.right)
