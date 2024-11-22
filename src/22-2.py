from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()

        # 이 블록들을 먼저 해제하기 위해 홀수 Lock과 짝수 Lock을 먼저 얻는다.
        self.odd_lock.acquire()
        self.even_lock.acquire()

    # printNumber(x)는 x를 출력한다. 여기서 x는 정수이다.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
