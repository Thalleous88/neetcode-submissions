# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        lst = []
        res = []
        def recur(root, subRoot, lst):

            if False in lst:
                return

            if (root is None and subRoot is not None) or (root is not None and subRoot is None):
                lst.append(False)
                return

            if root is None and subRoot is None:
                lst.append(True)
                return


            if root.val == subRoot.val:
                lst.append(True)
            else:
                lst.append(False)
                return
            

            recur(root.left, subRoot.left, lst)
            recur(root.right, subRoot.right, lst)
        
        def check(lst, res):
            count = 0
            for i in lst:
                if i == False:
                    res.append(False)
                    return
                else:
                    count += 1
                
            if (count == len(lst)):
                res.append(True)

        def preorder(root, subRoot, lst):
            if root != None:
                lst.clear()
                recur(root, subRoot, lst)
                check(lst, res)

                preorder(root.left, subRoot, lst)
                preorder(root.right, subRoot, lst)


        preorder(root, subRoot, lst)

        for i in res:
            if i == True:
                return True
        
        return False