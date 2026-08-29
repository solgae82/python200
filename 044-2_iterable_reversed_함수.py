# reversed(iter) 는 역순의 iterator를 반환(역순정렬이 아님, 정렬된 리스트 역순 리스트 반환)

# 리스트 역순, (모든 시퀀스 가능)
n_list = [8,3,9]
rn_list_iter = reversed(n_list)
print(type(rn_list_iter)) # <class 'list_reverseiterator'>

for v in rn_list_iter: 
    print(v , end=",") # 9,3,8,

print()

# 딕셔너리 역순(python 3.8 부터 가능,이전 버전엔 순서가 없었음)
fruits = {2:'사과', 3:'배',1:'수박'}
rev = reversed(fruits) # 키값 역순 반환
print(type(rev)) # <class 'dict_reversekeyiterator'>

for v in rev: 
    print(v , end=",") # 1,3,2

# 셋은 순서가 없으므로 reversed() 사용 못함
fruits = {'사과','배','참외'}
# rev = reversed(fruits) # TypeError: 'set' object is not reversible