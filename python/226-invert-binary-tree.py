# Diketahui:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

# Ditanya: Given the root of a binary tree, invert the tree, and return its root.

# Batasan:
# 1 <= Node.val <= 100
# The number of nodes in the tree is in the range [0, 100].

# Dijawab:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Penjelasan:
# 1. Kita mendefinisikan class Solution dengan method invertTree yang menerima satu parameter root.
# 2. Jika root adalah None, kita mengembalikan None.
# 3. Kita menukar posisi left dan right dari root dengan memanggil fungsi invertTree secara rekursif pada child node.
# 4. Kita mengembalikan root yang sudah di-invert.
# 5. Fungsi ini akan mengembalikan root dari binary tree yang sudah di-invert.
# 6. Fungsi ini menggunakan pendekatan rekursif untuk membalikkan binary tree.
