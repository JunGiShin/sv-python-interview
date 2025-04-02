class Solution:
    # @param {int} n，1개의 정수
    # @param {int[][]} edges，무방향 그래프
    # @return {boolean} 유효한 트리이면 True를 반환하고, 그렇지 않으면 False를 반환한다.
    def validTree(self, n, edges):
        root = [i for i in range(n)]  # 각 노드의 상위 노드를 초기화한다.
        for i in edges:  # 각 가장자리를 통과
            root1 = self.find(root, i[0])
            root2 = self.find(root, i[1])
            if root1 == root2:  # 이 간선의 두 점이 연결되어 있음을 나타낸다.
                return False
            else:
                root[root1] = root2
        return len(edges) == n - 1

    def find(self, root, e):
        if root[e] == e:
            return e
        else:
            root[e] = self.find(root, root[e])
            return root[e]
