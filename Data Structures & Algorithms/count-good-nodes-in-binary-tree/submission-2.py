# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        base = root.val
        lst = [0]
        def preorder(root, counter, base):
            if root != None:
                if root.val >= base:
                    counter += 1
                    lst[0] += 1
                    base = root.val

                

                preorder(root.left, counter, base)
                preorder(root.right, counter, base)

            return counter


        preorder(root, 0, base)

        return lst[0]
