class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.cnt = 0


class Solution:
    def _build(self, left, right):
        root = SegmentTreeNode(self.cumsum[left], self.cumsum[right])
        if left == right:
            return root

        mid = (left + right) // 2
        root.left = self._build(left, mid)
        root.right = self._build(mid + 1, right)
        return root

    def _print(self, root):
        if not root:
            return
        self._print(root.left)
        self._print(root.right)

    def _update(self, root, val):
        if not root:
            return
        if root.low <= val <= root.high:
            root.cnt += 1
            self._update(root.left, val)
            self._update(root.right, val)

    def _query(self, root, lower, upper):
        if lower <= root.low and root.high <= upper:
            return root.cnt
        if upper < root.low or root.high < lower:
            return 0
        return self._query(root.left, lower, upper) + self._query(
            root.right, lower, upper
        )

    # prefix-sum + SegmentTree | O(nlogn)
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1] + n)

        self.cumsum = sorted(list(set(cumsum)))
        root = self._build(0, len(self.cumsum) - 1)
        self._print(root)
        res = 0
        for csum in cumsum:
            res += self._query(root, csum - upper, csum - lower)
            self._update(root, csum)
        return res
