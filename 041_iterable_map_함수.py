
# 반복 가능 자료의 모든 요소를 특정 함수로 입력,반환 재처리 하는 map() 함수
# map (처리함수, iterable) => map 객체 반환

def my_func(x): 
    return x ** 2

result_map = map(my_func, [0,1,2,3])
print(type(result_map), result_map) # <class 'map'> <map object at 0x0000018F2A995420>
print(type(result_map), list(result_map)) # <class 'map'> [0, 1, 4, 9]

# 람다 함수로 구현
result_map = map(lambda x: x ** 2 , [0,1,2,3])
print(type(result_map), list(result_map)) # <class 'map'> [0, 1, 4, 9]

# iterable이 두개일때 map() 구현

x = [1,2,3,4,5] # 총 5개
y = [10,9,8,7]  # 총 4개
result_map = map(lambda x,y: (x ** 2) + y, x, y)
print(type(result_map), list(result_map))
# <class 'map'> [11, 13, 17, 23] , 인수가 모자라면 처리하지 않는다

x = [1,2,3,4,5] # 총 5개
y = [10,9,8,7,6]  # 총 4개
result_map = map(lambda x,y: (x ** 2) + y, x, y)
print(type(result_map), list(result_map))
# <class 'map'> [11, 13, 17, 23, 31]


