# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def height(root):
            if root is None:
                return 0

            l = height(root.left)
            r = height(root.right)

            return 1 + max(l, r)

        lst = [True]
        def preorder(root):
            if root != None:
                l = height(root.left)
                r = height(root.right)
                if abs(l-r) > 1:
                    lst[0] = False
                
                preorder(root.left)
                preorder(root.right)

        preorder(root)

        return lst[0]
        