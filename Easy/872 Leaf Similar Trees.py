Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def findLeaf(self, root):
		visited = [root]
		result = []
		while len(visited) > 0:
			node = visited.pop()
			if node.left:
				visited.append(node.left)
			if node.right:
				visited.append(node.right)
			if not node.left and not node.right:
				result.insert(0, node.val)
				
		return result
	
	def leafSimilar(self, root1, root2):
		"""
		dtype root1: TreeNode
		dtype root2: TreeNode
		rtype: bool
		"""
		return self.findLeaf(root1) == self.findLeaf(root2)
		
