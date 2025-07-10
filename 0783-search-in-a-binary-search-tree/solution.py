# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def search(self,root,val):
        if root==None:
            self.find=None
            return
        if root.val==val:
            self.find=root
            return
        if val<root.val:
            self.search(root.left,val)
        else:
            self.search(root.right,val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.find=None
        self.search(root,val)
        return self.find
