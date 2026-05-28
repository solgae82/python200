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

