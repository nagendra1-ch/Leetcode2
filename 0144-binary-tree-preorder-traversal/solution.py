# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,root,result):
        if root==None:
            return
        result.append(root.val)
        self.pre(root.left,result)
        self.pre(root.right,result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.pre(root,result)
        return result
