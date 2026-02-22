"""
for 문에 사용되는 자료는 반복(iterable) 가능한 객체여야 한다
    -시퀀스자료형(리스트,튜플,문자열,range(),바이너리 시퀀스)
    -딕셔너리
    -Set
    -그 외 반복 가능 객체
"""

#문자열
str_data = 'abc'
for c in str_data: 
    print(c , end="/") # a/b/c/

print()

#리스트
list_data = [1,2,3,4,5]
for i in list_data:
    print(i,end='-') #1-2-3-4-5-

print()

#튜플
tuple_data = (1,2,3)
for t in tuple_data: 
    print(t, end='-') #1-2-3-

print()

#딕셔너리
dict_data = {1:'한글',2:'영어'}
for k,v in dict_data.items():
    print(k,':',v , sep='', end ='|') # 1:한글|2:영어|

print()

for dic in dict_data.items(): #튜플 반환
    print(dic , end ='|') #(1, '한글')|(2, '영어')|

print()

#range()
for i in range(2,10):
    print(i, end='') #23456789


print()

"""
    반복문에 사용가능한 continue , break
"""

for i in [1,2,3,4,5]: 
    print(i,end='') # 12
    if i < 2: 
        continue
    else: 
        break

print()

for i in [1,2,3,4,5]: 
    print(i, end='') # 12
    if i == 2: break

    