# LifoQueue 기반 스택 구현
from queue import LifoQueue

# 스택 초기화
stack = LifoQueue(maxsize=3)

# qsize()로 스택의 원소 수를 나타낸다.
print(stack.qsize())

# put() 함수로 원소를 스택에 push한다.
stack.put("a")
stack.put("b")
stack.put("c")
print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() 함수로 스택에서 원소를 pop한다.
print("\nElements popped from the stack")
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ", stack.empty())
