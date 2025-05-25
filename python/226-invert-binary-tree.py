class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.val, end=" ")
            self.printTree(root.right)

# Membuat TreeNodes untuk pengujian
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

root3 = None

sol = Solution()

print("Pohon 1 sebelum diinvert:")
sol.printTree(root1)
inverted_root1 = sol.invertTree(root1)
print("\nPohon 1 setelah diinvert:")
sol.printTree(inverted_root1)
print("\n")

print("Pohon 2 sebelum diinvert:")
sol.printTree(root2)
inverted_root2 = sol.invertTree(root2)
print("\nPohon 2 setelah diinvert:")
sol.printTree(inverted_root2)
print("\n")

print("Pohon 3 sebelum diinvert:")
sol.printTree(root3)
inverted_root3 = sol.invertTree(root3)
print("\nPohon 3 setelah diinvert:")
sol.printTree(inverted_root3)
print("\n")