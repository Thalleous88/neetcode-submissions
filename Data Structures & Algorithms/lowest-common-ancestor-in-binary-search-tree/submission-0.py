# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def lca(root, p, q):
            if not root:
                return None
            
            if root.val == p.val or root.val == q.val:
                return root

            leftLca = lca(root.left, p, q)
            rightLca = lca(root.right, p, q)

            if leftLca and rightLca:
                return root

            return leftLca if leftLca else rightLca
            

        return lca(root, p, q)