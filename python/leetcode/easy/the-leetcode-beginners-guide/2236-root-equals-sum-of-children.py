# Diketahui:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        

# Ditanya:
# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

# Dijawab:
        return root.val == (root.left.val + root.right.val) if root.left and root.right else False
    
# Penjelasan:
# 1. Kita mendefinisikan class Solution dengan method checkTree yang menerima parameter root.
# 2. Kita memeriksa apakah root memiliki anak kiri dan kanan.
# 3. Jika iya, kita membandingkan nilai root dengan jumlah nilai anak kiri dan kanan.