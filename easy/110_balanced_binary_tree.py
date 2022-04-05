class Solution:
    def isBalanced(self, root):
        if root:
            return True
        
        return (abs(self.treeHeight(root.left) - self.treeHeight(root.right)) < 2)\
        and self.isBalanced(self.left)\
        and self.isBalanced(self.right)

    def treeHeight(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.treeHeight(node.left), self.treeHeight(node.right))

# Check whether root node the height is balanced 
# Then check the left/right sub-tree is balanced or not 
