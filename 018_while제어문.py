"""
    while 조건: 
        # True일때 실행되는 반복 코드
        continue # while문 처음으로 이동, 다시 반복 반복 코드 실행
        break # while문 탈출
"""

x = 0
while x < 10: 
    x = x + 1
        
    if x < 5:
        continue

    print(x, end='') #567

    if x > 6:
        break

print()

x = 0
total = 0
while True:
    print(x , end='') #012345
    x = x + 1
    total = total + x
    if x > 5: break

print()
print('합계: ' + str(total)) #합계: 21
