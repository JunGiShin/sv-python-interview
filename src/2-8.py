class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)  # 문자열 a의 길이
        len_b = len(b)  # 문자열 b의 길이
        # 둘 중 어느 것이 더 긴지 비교
        max_length = max(len_a, len_b)
        carry = 0  # carry 값 초기화
        new_str = []
        for i in range(-1, -max_length - 1, -1):  # 문자열을 오른쪽에서 왼쪽으로 탐색
            element_a = 0
            element_b = 0
            if abs(i) <= len_a:
                element_a = a[i]  # a 위치의 문자열값을 가져온다.
            if abs(i) <= len_b:
                element_b = b[i]  # b 위치의 문자열값을 가져온다.
            # 문자열 a와 b의 값과 carry를 더한다.
            add = int(element_a) + int(element_b) + int(carry)
            value = add % 2  # 현재 위치의 나머지
            carry = add // 2  # 올림값
            new_str.insert(0, str(value))  # 새 문자열의 시작 부분에 새로 생성된 값을 삽입한다.
        if carry != 0:  # 마지막으로 carry 플래그가 0이 아닌 경우를 주의한다.
            new_str.insert(0, str(carry))
        return ''.join(new_str)
