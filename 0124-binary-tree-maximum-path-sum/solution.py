# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,root):
            if root == None:
                return 0

            leftSum = self.recur(root.left)
            rightSum = self.recur(root.right)

            curveSum = root.val + leftSum + rightSum
            nodeSum = max(root.val , root.val + max(leftSum , rightSum))
            
            self.maxi = max(self.maxi , curveSum , nodeSum , root.val)

            return nodeSum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=root.val
        self.recur(root)
        return self.maxi
