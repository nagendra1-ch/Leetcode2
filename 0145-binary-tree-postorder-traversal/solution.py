# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def post(self,root,result):
        if root==None:
            return
        self.post(root.left,result)
        self.post(root.right,result)
        result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.post(root,result)
        return result
