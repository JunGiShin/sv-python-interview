from queue import PriorityQueue

customers = PriorityQueue()
# 함수를 사용하는 대신 OOP 스타일로 PriorityQueue 클래스를 초기화하고 원소를 넣는다.
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
while not customers.empty():
    # Riya, Harry, Charles, Stacy 순으로 이름을 출력한다.
    print(customers.get())
