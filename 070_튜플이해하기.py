
# 리스트와 비슷하지만, 요소 값을 변경할 수 없는 immutable이다

tuple_data = 1, "two", '셋'
print(tuple_data) # (1, 'two', '셋')

tuple_data = (1, "two", '셋')
print(tuple_data) # (1, 'two', '셋')

# 변수 분기
x,y,z = tuple_data
print(x,y,z) # 1 two 셋

# 요소 변경하려고 하면 에러 
# tuple_data[1] = '삼' # TypeError: 'tuple' object does not support item assignment