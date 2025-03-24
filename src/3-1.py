stack = []

# append() 함수는 리스트(스택)의 가장 뒤(위)에 원소를 추가한다.
# 스택에 원소를 추가한다.
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial stack")
print(stack)

# pop() 함수는 스택의 가장 뒤(위)의 원소를 추출한다.
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nStack after elements are popped:")
print(stack)
