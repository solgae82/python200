
# yield 키워드가 있는 함수가 제네레이터이다
# yield 키워드는 값 반환(return) + 프로세스 중단 기능을 한다.
# 함수 호출시 모두 처리 후 반환이 아닌, 현재값 반환 -> 중단 -> 재호출시 중단 프로세스 재시작 사이클을 돈다.
# 메모리에 결과를 모두 올려서 사용하는 일반함수와 다른 알뜰한 효율을 자랑한다.
# 매우 큰 데이터를 반복 처리 해야할때 필수 기능이라 할 수 있다.

def Myrnage(n): 
    current = 0
    while current < n:
        yield current
        current +=1


int_list = Myrnage(5)
for i in int_list: 
    print(i, end='') # 01234