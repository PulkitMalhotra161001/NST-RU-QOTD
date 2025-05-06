https://my.newtonschool.co/playground/code/l4hr7gek3td3


class Solution:
    def maxDepthBinaryTree(self, root):
        if root==None:
            return 0
        height =1+ max(self.maxDepthBinaryTree(root.left), self.maxDepthBinaryTree(root.right))
        return height
    def minBinaryTree(self, root):
        if root==None:
            return 100000000000
        Min = min(root.key , self.minBinaryTree(root.left), self.minBinaryTree(root.right))
        return Min
    def sizeBinaryTree(self, root):
        if root==None:
            return 0
        size = 1+ self.sizeBinaryTree(root.left)+ self.sizeBinaryTree(root.right)
        return size
