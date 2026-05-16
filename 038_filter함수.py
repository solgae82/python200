
# filter(체크함수[True/False], 이터러블객체)
# 특정 조건을 만족하는 필터링된 이터레이터 객체 반환

# 체크함수 구현
def getPrime(x): 
    if x == 2: 
        return True
    if x <=1 or x % 2 == 0: 
        return False
    
    for i in range(3, int(x**(1/2)) + 1 , 2):
        if x % i == 0:
            return False
        
    else: 
        return True
    

int_list = [x for x in range(1, 101)] # 1~100
ret = filter(getPrime , int_list)

for i in ret: 
    print(i, end=',') 
    # 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,