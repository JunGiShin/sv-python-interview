# Array 중에서 k개 원소를 무작위로 선택한다.
import random


# Array를 인쇄하는 함수 구현
def printArray(stream, n):
    for i in range(n):
        print(stream[i], end=" ")
    print()


# Array [0..n-1]에서 k개의 원소를 무작위로 추출하는 함수 구현
def selectKItems(stream, n, k):
    # 초기 단계: 처음 k개의 항목을 reservoir에 저장
    reservoir = [stream[i] for i in range(k)]
    
    # 이후 항목들 처리: k번째부터 n-1번째 항목까지
    for i in range(k, n):
        j = random.randrange(i + 1)
        if j < k:
            reservoir[j] = stream[i]
    
    print("Following are k randomly selected items")
    printArray(reservoir, k)
    
# main 함수
if __name__ == "__main__":
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(stream)
    k = 5
    selectKItems(stream, n, k)
