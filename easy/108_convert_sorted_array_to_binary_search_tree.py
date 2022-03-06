class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        n = len(nums)
        m = n // 2

        # Use mid value as parent/root node of subtree
        res = TreeNode(nums[m])

        # Grow lefr and right tree together will ensure the height is balanced
        # The left node of a root/parent node will be a root/parent node of its subtree
        res.left = self.sortedArrayToBST(nums[:m])
        res.right = self.sortedArrayToBST(nums[m+1:])

        return res

    def v2(self, nums):
        def helper(left, right):
            if left > right:
                return None

            # Use left middle node as a root for a subtree
            m = (left + right) // 2

            # Do a pre-order traversal
            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)

            # Return the root node
            return root
        
        # Traverse the whole list 
        return helper(0, len(nums)-1)
