
# 이터러블 객체 요소가 모두 수치형일때 sum 함수로 총합을 추출할 수 있다.

num_list = [1,3,5,7,9]
ret = sum(num_list)
print(ret) # 25

ret = sum(num_list, 10)
print(ret) # 35

random_list = [1,2,'a'] # 계산 안되는 문자
#ret = sum(random_list) # TypeError: unsupported operand type(s) for +: 'int' and 'str' 
