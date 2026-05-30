# 삼중 (쌍)따옴표는 주석뿐 아니라, 여려행 문자열 지정에도 쓰인다

str_data='안녕하세요. "헤이맨!" 이라고' 
print(str_data) # 안녕하세요. "헤이맨!" 이라고

# 삼중 따옴표는 같은 형식의 ''를 데이터로 쓸 수 있다.
str_data1='''안녕하세요. 
'헤이맨!' 이라고[1]
'''

# 삼중 쌍 따옴표는 같은 형식의 ""를 데이터로 쓸 수 있다.
str_data2="""안녕하세요. 
"헤이맨!" 이라고[2]
"""

print(str_data1)
print(str_data2) 

"""
안녕하세요. 
'헤이맨!' 이라고[1]

안녕하세요. 
"헤이맨!" 이라고[2]

"""
# 위 2개 문장 마지막에 개행문자가 들어간 것을 알 수 있다.


# 한줄 문자열을 여러줄로 표현, 리눅스 명령어 연결과 비슷
s_coments = 'a' \
'b' \
'c'
print(s_coments) # abc

s_coments = 'd\
e\
f\
'
print(s_coments) # def


# 문자열에서 이스케이프 개행 문자 넣기
str_data ="동해물과 백두산이\n마르고 닳도록"
print(str_data)
'''
동해물과 백두산이
마르고 닳도록
'''
# 문자 => 코드값 변환
code = ord('a')
print(type(code), code) # <class 'int'> 97

# 코드값 => 문자 변환
c_data = chr(97)
print(type(c_data), c_data) # <class 'str'> a

# f '' 포맷, {변수} 출력
t = '동이'
print(f'내 이름은 {t} 여') # 내 이름은 동이 여

# f'' 포맷, 소숫점 포맷 
pi = 3.141592
print(f'원주율 {pi}')   # 원주율 3.141592
print(f'원주율 {pi:.2f}') # 원주율 3.14

# f'' 포맷, 십진수 천 단위마다 ',' 넣기
n_pop = 3789911
print(f'서울: {n_pop:,d}명') #서울: 3,789,911명

# '문자열'.format()
pi = 3.141592
n_pop = 3789911

text = '{} 근사값은 {} 입니다'.format('원주율', pi)
print(text) # 원주율 근사값은 3.141592 입니다

text = '{} 근사값은 {:.2f} 입니다'.format('원주율', pi)
print(text) # 원주율 근사값은 3.14 입니다

text = '{}: {:,d}명'.format('서울', n_pop)
print(text) # 서울: 3,789,911명


# find('문자열')=> 전체 문자열에서 주어진 '문자열' 위치 정수 반환
# index()와 차이는 
# index()는 시퀀스와 문자열 모두 가능, find()는 문자열 전용
# 값이 없을때 index()는 ValueError, find()는 -1 반환

str_data = "A lot of things occur each day! every day!"

print(str_data.index('day')) # 27
print(str_data.find('day')) # 27
print(str_data.find('day', 28)) # 38

#print(str_data.index('fighter')) # ValueError: substring not found
print(str_data.find('fighter')) # -1


# 문자열 인코딩, 디코딩
import sys

# 1. 글자당 몇 바이트짜리 구조체를 썼는지 확인 (기본 문자 크기)
# sys.getsizeof() 공식 문서에 따른 문자 속성 검사 방식으로 추정 가능.
# 파이썬 내부적으로 쓰는 구조체 헤더 + 문자바이트 공식이기 때문에 자주 변하고 알 필요도 없음.
# 인간은 인간에게 편리한 논리적인 매카니즘으로만 게산하면 됨.
# 현재 테스트는 파이썬 3.12 버전임.

str_data = 'python'
print(f"글자 수: {len(str_data)}글자") # 글자 수: 6글자
print(f"실제 메모리 총 크기: {sys.getsizeof(str_data)} 바이트") # 실제 메모리 총 크기: 47 바이트

str_data = 'pyth한글'
print(f"실제 메모리 총 크기: {sys.getsizeof(str_data)} 바이트") #실제 메모리 총 크기: 70 바이트

str_data = 'pyth😀😁'
print(f"실제 메모리 총 크기: {sys.getsizeof(str_data)} 바이트") # 실제 메모리 총 크기: 84 바이트

print(len('pyth한글')) # 6 <= 인간은 이렇게만 인식하면 됨.


str_data = '파이썬'
byte_data = str_data.encode('UTF-8')
print(byte_data ,'/' , len(byte_data)) #b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac' / 9

for k,v in enumerate(byte_data): 
    print(k, '=>', v) # v 는 UTF-8로 인코딩된 바이너리(byte) 값을 보여줌.
'''
0 => 237
1 => 140
2 => 140
3 => 236
4 => 157
5 => 180
6 => 236
7 => 141
8 => 172
'''

str_data = '파이썬'
byte_data = str_data.encode('CP949')
print(byte_data ,'/' , len(byte_data)) # b'\xc6\xc4\xc0\xcc\xbd\xe3' / 6

for k,v in enumerate(byte_data): 
    print(k, '=>', v) # v 는 UTF로 인코딩된 바이너리(byte) 값을 보여줌.
'''
0 => 198
1 => 196
2 => 192
3 => 204
4 => 189
5 => 227
'''


# 현 시스템 빅엔디언(big), 리틀엔디언(little) 확인 (현재 인텔 CPU)
print(sys.byteorder) # little

