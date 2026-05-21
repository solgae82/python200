
# 시퀀스 자료 일부 범위를 취하는 slicing 기법
# [시작인덱스:끝 인덱스] = 끝 인덱스 - 1까지만 자른다

str = 'I love phython'
print(str[0:4]) # I lo 
print(str[7:9]) # ph
print(str[:5])  # I lov
print(str[7:])  # phython
print(str[:-6]) # I love p
print(str[-3:]) # hon

# 전체 범위 자르기 후 step 2 필터링
print(str[::2]) # Ilv hto

n_list = [0,1,2,4,5,6,7,8,9]
print(n_list[2::2]) # [2, 5, 7, 9]