
# 시퀀스 자료형에서 max(), min() 사용하기

n_list = [32,0,99,48]
print(max(n_list)) # 99 
print(min(n_list)) # 0

str_data = 'ILoveYou'
print(max(str_data)) # v
print(min(str_data)) # I

str_list = ['3sung', 'sam', 'World']
print(max(str_list)) # sam
print(min(str_list)) # 3sung

# 같은 자료형이 아닌데, max(), min() 쓰면 에러
com_list = ['a', 22, 'F']
#print(max(com_list)) # TypeError: '>' not supported between instances of 'int' and 'str'
#print(min(com_list)) # TypeError: '<' not supported between instances of 'int' and 'str'
