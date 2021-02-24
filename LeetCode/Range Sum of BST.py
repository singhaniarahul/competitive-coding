# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if(root == None):
            return 0
        sumOfCurrentTree = 0
        if(root.val>=low and root.val<=high):
            sumOfCurrentTree += root.val
        if(root.left != None or root.right!= None):
            sumOfCurrentTree += (self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high))
        return sumOfCurrentTree
