#자료형
"""
수치자료(Numeric Type)
"""
intData=15 #정수형
floatData = 2.5 #실수 데이터
complexData = 1 + 1j #복소수 데이터 

"""
불리언 자료(Boolean Type)
"""
isTrue = True
isFalse = False

"""
시퀀스 자료(Sequence Type)
    : 순서가 있는 요소들로 구성된 자료형
    : 정수 index로 접근 가능
    : 자료의 크기, 길이가 있다
    종류
        list
        튜플
        문자열,
        range 객체
        바이너리 시퀀스
    (설명하게 많은 주제이므로 대충 형태만 보자)
"""

list = [10,20,30] #리스트

tuple = ('하늘','땅') #튜플

#문자열
string = "Hello"
for char in string:
    print(char,end='/') #H/e/l/l/o/

print() #한칸띄기

#range
for i in range(5):
    print(i, end='') #01234

print() #한칸띄기

# 바이너리시퀀스 중 bytes (불변)
b = b"hello"
print(b[0]) # 104 ('h'의 아스키 코드)

"""
Set 자료형
    : 수학의 집합요소처럼, 순서는 없고 중복되지 않는 요소들
"""
setData = {1,2,3,4,5}

"""
Dictionary 자료형
    : 키,값으로 구성된 자료형
"""
dictData = {0:False, 1:True}

"""
iterable 자료형
    : 반복 가능 자료형을 뜻한다.
    : for문에서 in 다음에 사용될 수 있는 자료형
    : 시퀀스 자료형 , Set 자료형, Dictionary 자료형 은 iterable 이다
    : list() 함수로 iterable 자료형을 리스트로 변환 가능
"""