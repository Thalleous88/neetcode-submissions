# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        order = 0
        ans = root.val
        def inorder(root):
            nonlocal order
            nonlocal ans
            if root:
                inorder(root.left)
                order += 1
                if order == k:
                    ans = root.val
                inorder(root.right)


        inorder(root)

        return ans

        

