"""
generator : iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함

yield 키워드는 Python에서 제너레이터(Generator) 함수를 정의할 때 사용되는 특별한 키워드입니다. 
제너레이터는 이터레이터(Iterator)의 한 종류로, 값을 한 번에 모두 메모리에 저장하는 대신, 필요할 때마다 하나씩 생성하여 반환합니다.
출처: https://bcho.tistory.com/1460 [조대협의 블로그:티스토리]
"""

def test_generator(): 
    yield 1
    yield 2
    yield 3

gen = test_generator()
print(type(gen)) #<class 'generator'>
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
#print(next(gen)) # StopIteration 예외 발생

#generator를 동시에 두개 생성하면, 서로가 다른 객체이며, 각기 따로 동작합니다.
gen_1 = test_generator()
gen_2 = test_generator()

print(gen_1 == gen_2) # False
print(next(gen_1)) # 1
print(next(gen_2)) # 1
print(next(gen_1)) # 2

# 리스트 컴프리헨션
squares_list = [x**2 for x in range(10)] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares_list)

# 제너레이터 표현식
squares_gen = (x**2 for x in range(10))
print(squares_gen) #제네레이터 객체, <generator object <genexpr> at 0x000002105F888E10>
for i in squares_gen: 
    print(i, end='/') #0/1/4/9/16/25/36/49/64/81/


print('--------')

# yield from (Python 3.3 이상)
# 다른 제네레이터나 이터러블 객체로부터 yield 할때 사용
def chain_generator(gen1, gen2): 
    yield from gen1
    yield from gen2

gen_1 = (i for i in range(3))
gen_2 = (i for i in range(3,6))

chain = chain_generator(gen_1, gen_2)

for val in chain: 
    print(val, end='/') # 0/1/2/3/4/5/


print('--------')

# 요리 제너레이터 
def make_pizza():
    print("피자 도우 준비")
    yield "도우"  # 도우 준비 완료, 호출자에게 도우를 주고 잠시 대기
    print("토핑 추가")
    yield "토핑"  # 토핑 추가 완료, 호출자에게 토핑을 주고 잠시 대기
    print("피자 굽기")
    yield "완성된 피자"  # 피자 완성, 호출자에게 피자를 줌

pizza_gen = make_pizza()

step1 = next(pizza_gen)  # "피자 도우 준비" 출력, "도우" 반환, 실행 중단
print(f"지금까지: {step1}") # 지금까지: 도우

step2 = next(pizza_gen)  # (중단된 위치에서 다시 시작) "토핑 추가" 출력, "토핑" 반환, 실행 중단
print(f"지금까지: {step1}, {step2}") # 지금까지: 도우, 토핑

step3 = next(pizza_gen) # (중단된 위치에서 다시 시작) "피자 굽기" 출력, "완성된 피자" 반환, 실행 중단
print(f"지금까지: {step1}, {step2}, {step3}") # 지금까지: 도우, 토핑, 완성된 피자

#핵심은 이거다
#무한 수열
def infinite_seqence(): 
    num = 0
    while True:
        yield num
        num = num + 1

infinite_gen = infinite_seqence()
print(next(infinite_gen)) # 0
print(next(infinite_gen)) # 1
print(next(infinite_gen)) # 2
#..
# 일반 함수였다면 무한 루프로 메모리가 꽉 차서 프로그램 종료되겠지만, 제네레이터는 가능하다

