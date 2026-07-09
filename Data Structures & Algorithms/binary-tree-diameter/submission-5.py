# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root):
            if root is None:
                return 0

            l = height(root.left)
            r = height(root.right)

            return 1 + max(l, r)

        def maxh(root):
            return height(root.left) + height(root.right)

        lst = [0]
        def preorder(root, lst):
            if root != None:
                if (lst[0] < maxh(root)):
                    lst[0] = maxh(root)
                    
                
                preorder(root.left, lst)
                preorder(root.right, lst)
            

            return lst[0]

    


        return preorder(root, lst)
            
