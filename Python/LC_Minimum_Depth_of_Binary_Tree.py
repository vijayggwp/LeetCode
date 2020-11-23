# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        Approach:
        
        Crucial point is that, if left is present and right is not present, you gotta consider the left and not the right.
        Draw the tree and you'll understand why.
        
        """
        if not root:
            return(0)
        elif(not root.left or not root.right):
            return(max(self.minDepth(root.left),self.minDepth(root.right))+1)
        else:
            return(min(self.minDepth(root.left),self.minDepth(root.right))+1)
            