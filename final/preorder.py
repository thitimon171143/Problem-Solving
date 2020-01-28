def PreorderTraversal(self, root):
    res = []
    if root:
        res.append(root.data)
        res = res + self.preorderTraversal(root.left)
        res = res + self.PreorderTraversal(root.right)
    return res