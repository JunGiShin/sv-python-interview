class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        table = {}
        # 노드의 인덱스값 기록
        table[head] = Node(head.val)

        # 원본을 가리키는 curr을 선언
        curr = head

        while curr:
            copy = table[curr]

            # 다음 가리키는 노드가 있다면,
            if curr.next is not None:
                # 다음 가리키는 노드가 해시 테이블에 없다면(방문하지 않은 노드라면),
                if curr.next not in table:
                    # 복사본에 복사하고 해시 테이블에 기록한다.
                    copy.next = Node(curr.next.val)
                    table[curr.next] = copy.next
                # 이미 방문한 노드라면, 복사본에 업데이트한다.
                else:
                    copy.next = table[curr.next]

            if curr.random is not None:
                if curr.random not in table:
                    copy.random = Node(curr.random.val)
                    table[curr.random] = copy.random
                else:
                    copy.random = table[curr.random]

            copy = copy.next
            curr = curr.next

        return table[head]
