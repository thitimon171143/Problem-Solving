def PostorderTraversal(self,root):
    res = []
    if root:
        res = self.PostorderTraversal(root.left)
        res = res+self.PostorderTraversal(root.right)
    return res