"""
for 변수 in 범위: 
    반복 실행 코드
else: 
    for문 반복 실행 코드가 범위만큼 빠짐없이 실행되었을 경우 실행되는 코드
"""

for x in [1,2,3]: 
    print(x, end="") #123
else: 
    print()
    print('모두 실행') #모두 실행


for x in [1,2,3]: 
    print(x , end='') #12
    if x == 2: break
else: 
    print('모두 실행') #실행 안됨