class Solution:
    def postorderTraversal(self, root):  # 후위 순회
        if not root:
            return []
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )
