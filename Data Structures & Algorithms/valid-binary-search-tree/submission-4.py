# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(root, min, max):
            if not root:
                return True

            if root.left and root.val <= root.left.val:
                return False
            
            if root.right and root.val >= root.right.val:
                return False

            if root.val <= min or root.val >= max:
                return False

            left = isvalid(root.left, min, root.val)
            right = isvalid(root.right, root.val, max)

            

            return (left and right)

        
        return isvalid(root, float('-inf'), float('inf'))
            