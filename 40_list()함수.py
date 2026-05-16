
# 모든 이터러블 객체(시퀀스,문자열,dictionary,set,binary sequence)는 list()로 리스트로 변환 할 수 있다
# 제너레이터도 list() 로 리스트 변환 가능.

tupleData = (1,2,3)
listData = list(tupleData)
print(type(listData), listData, sep=",") # <class 'list'>,[1, 2, 3]

strData = 'I love python'
listData = list(strData)
print(type(listData), listData, sep=",") 
#<class 'list'>,['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']

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
