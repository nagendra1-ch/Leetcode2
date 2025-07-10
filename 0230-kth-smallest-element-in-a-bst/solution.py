# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,k):
        if root==None:
            return
        self.inorder(root.left,k)
        self.result.append(root.val)
        if len(self.result)==k:
            self.ans=root.val
        self.inorder(root.right,k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result=[]
        self.ans=0
        self.inorder(root,k)
        if len(self.result)<k:
            return -1
        return self.ans
