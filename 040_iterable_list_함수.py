
# 모든 이터러블 객체(시퀀스,문자열,dictionary,set,binary sequence)는 list()로 리스트로 변환 할 수 있다
# 제너레이터도 list() 로 리스트 변환 가능.

# 시퀀스: 튜플
tupleData = (1,2,3)
listData = list(tupleData)
print(type(listData), listData, sep=",") # <class 'list'>,[1, 2, 3]

# 시퀀스: 문자열
strData = 'I love python'
listData = list(strData)
print(type(listData), listData, sep=",") 
#<class 'list'>,['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']

# 시퀀스:generator
# 제너레이터 -> 리스트 변환
def Myrange(n):
    current = 0
    while current < n :
        yield current 
        current += 1

int_my_list = Myrange(5)
print(type(int_my_list)) # <class 'generator'>

listData = list(int_my_list)
print(type(listData), listData, sep=',') # <class 'list'>,[0, 1, 2, 3, 4]

# set 자료형
set_data = {'사과','배','딸기'}
s_list = list(set_data)
print(type(s_list), s_list) # <class 'list'> ['배', '사과', '딸기']

# dictionary 자료형
dic_data = {'사과':10, '배': 20, '바나나': 15}
d_list = list(dic_data) # 기본 키값으로 리스트를 만든다
print(type(d_list), d_list) # <class 'list'> ['사과', '배', '바나나']

d_list = list(dic_data.items()) # 튜플로 리스트를 만든다
print(type(d_list), d_list) # <class 'list'> [('사과', 10), ('배', 20), ('바나나', 15)]

d_list = list(dic_data.keys()) # 명시적 키값으로 리스트를 만든다
print(type(d_list), d_list) # <class 'list'> ['사과', '배', '바나나']

d_list = list(dic_data.values()) # 명시적 값으로 리스트를 만든다
print(type(d_list), d_list) # <class 'list'> [10, 20, 15]

