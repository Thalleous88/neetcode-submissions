# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def height(root):
            if root is None:
                return 0

            l = height(root.left)
            r = height(root.right)

            return 1 + max(l, r)

        res = [[] for _ in range(height(root))]

        def preorder(root, counter):
            if root != None:
                res[counter].append(root.val)
                preorder(root.left, counter+1)
                preorder(root.right, counter+1)
            

            return res

        return preorder(root, 0)