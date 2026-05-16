
# 0,'',"",[],(),{},None 모두 거짓(False)

# all(iterable) 은 반복 자료가 모두 참일때 True
print(all([0,1,2,3])) # False
print(all([1,2,3])) # True

# any(iterable) 안 반복 자료 중 1개 이상 참이 있을때 True
print(any([0,'',"",[],{},None])) # False
print(any([1,'',"",[],{},None])) # True

