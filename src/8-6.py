class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            # 현재 노드의 다음 노드를 임시 변수 next에 저장하고,
            # 현재 노드의 next를 이전 노드(prev)로 변경한다.
            next, node.next = node.next, prev
            # prev는 현재 노드로 업데이트하고, 현재 노드는 다음 노드로 업데이트한다.
            prev, node = node, next
        return prev
