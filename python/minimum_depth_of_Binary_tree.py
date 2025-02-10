'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(root,level):
            if not root.left and not root.right:
                return level 
            ans = 2**31
            if root.left:
                ans=min(ans,DFS(root.left,level+1))
            if root.right:
                ans=min(ans,DFS(root.right,level+1))
            return ans

        if not root:
            return 0
        return DFS(root,1)
    

    #
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        # Base case...
        # If the subtree is empty i.e. root is NULL, return depth as 0...
        if root is None:
            return 0
        # Initialize the depth of two subtrees...
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        # If the both subtrees are empty...
        if root.left is None and root.right is None:
            return 1
        # If the left subtree is empty, return the depth of right subtree after adding 1 to it...
        if root.left is None:
            return 1 + rightDepth
        # If the right subtree is empty, return the depth of left subtree after adding 1 to it...
        if root.right is None:
            return 1 + leftDepth
        # When the two child function return its depth...
        # Pick the minimum out of these two subtrees and return this value after adding 1 to it...
        # Adding 1 is the current node which is the parent of the two subtrees...
        return min(leftDepth, rightDepth) + 1
