
# 시퀀스 뿐만 아니라 dic, set 에서도 사용가능 
# (인덱스,요소)된 enumerate 객체 반환
# enumerate 객체 : CPython으로 구현된 이터레이터이면서 제너레이터 기능을 갖췄다
# 제너레이터와 유사한 지연 평가를 사용하므로 대용량 자료 처리에 좋다(메모리 효율 극대화)
# start=정수 옵션으로 시작 index 값을 설정할 수 있다.
# 빌트인 된 C언어 기반이므로 제네레이터보다 성능이 더 좋다.

# 시퀀스
n_list = [5, 7, 2]
for k, v in enumerate(n_list): 
    print(k,v)
"""
0 5
1 7
2 2
"""

# start 값 설정
for k, v in enumerate(n_list , start=101): 
    print(k,v)
"""
101 5
102 7
103 2
"""


# dictionary 에서는 key값을 기준으로 (index, key)를 만든다
dic = {'f-1':'사과', 'f-2':'배'}
enum =enumerate(dic)
print(type(enum)) # <class 'enumerate'>

print(dic.items()) # dict_items([(1, '사과'), (2, '배')])

for k,v in enum: 
    print(k , v , dic[v])
"""
0 f-1 사과
1 f-2 배
"""

# set 자료
n_set = {3,1,2}
enum = enumerate(n_set)
print(type(enum)) # <class 'enumerate'>

for k,v in enum: 
    print(k,v)
"""
0 1
1 2
2 3
"""

# enumerate 와 동일 기능의 제너레이터 구현하기
def myEnumerate(iter, start=1): 
    n = start
    for item in iter: 
        yield (n , item)
        n += 1

n_list = [3,8,4]
for k,v in myEnumerate(n_list, 201): 
    print(k,v)
"""
201 3
202 8
203 4
"""