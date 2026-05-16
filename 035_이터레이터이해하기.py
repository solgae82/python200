
# 모든 반복 가능 자료는 __iter__() 메서드로 iterator를 반환
listData = [1,2,3]
iter1 = listData.__iter__()
print(type(listData)) # <class 'list'>

# next(이터레이터) 로 요소 한개씩 호출
print(next(iter1)) # 1
print(next(iter1)) # 2
print(next(iter1)) # 3
#print(next(iter1)) # StopIteration 에러

# iter(반복자) 로 iterator 반환 
iter2 = iter(listData) # <list_iterator object at 0x000002C3AEC159C0>
print(iter2)

print(next(iter2)) # 1
print(next(iter2)) # 2
print(next(iter2)) # 3
#print(next(iter2)) # StopIteration 에러

# 이터레이터도 반복 가능 객체이다
iter3 = iter(listData)
for i in iter3:
    print(i , end="") # 123

