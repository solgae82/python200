print('안녕하세요 파이썬') #안녕하세요 파이썬

hello='Hello~!'
print(hello) #Hello~!

intData = 1
intData2 = 2
print(intData + intData2) #3

name ='홍길동'
phone = '010-1234-5678'
#[기본 출력으로 인수 사이에 '공백'이 들어간다]
print('이름:',name, ',', '폰:',phone) # 이름: 홍길동 , 폰: 010-1234-5678  

print('#', end='') #기본 마지막에 개행문자가 들어가는데, end=''로 줄바꿈 하지 않음.
print() #줄바꿈
print('ㅋ' * 5) # ㅋㅋㅋㅋㅋ

#[인수 사이 기본공백을 '/'로 변경]
print(name, phone, sep='/') #홍길동/010-1234-5678