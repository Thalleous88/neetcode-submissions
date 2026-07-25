# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(root1, root2):
            check = True
            if not root1 and not root2:
                return True
            elif (not root1 and root2) or (root1 and not root2):
                check = False
            elif root1.val != root2.val:
                check = False
            
            left = check and traverse(root1.left, root2.left)
            right = check and traverse(root1.right, root2.right)

            if left and right:
                return True
            else:
                return False


        

        return traverse(p, q)