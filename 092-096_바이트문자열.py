
# b'' 표현식으로 바이트 문자열 정의(ASCII만 가능), 파이썬 기본 문자 인코딩은 UTF-8
str_data = 'python'
byte_data = b'bython'
print(str_data[0] == byte_data[0]) # False
print(str_data[0] , byte_data[0])   # p 98
print(type(str_data[0]), type(byte_data[0])) # <class 'str'> <class 'bytes'>
# 이진수는 같지만, 타입이 달라서 해석값이 다르다.('p' == 98), 그래서 False다

# b'' 표현식 내부 값은 ASCII만 가능하다
# byte_data = b'파이썬' # SyntaxError: bytes can only contain ASCII literal characters

# 문자열.encode() 메소드로 바이트 문자열 정의(기본 UTF-8)
byte_data = '파이썬'.encode()
print(byte_data) # b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'

# 아래 표현식과 기본 encode()는 같은 인코딩(UTF-8)
print((b'python') == 'python'.encode()) # True

# 아래가 같게 나오는 이유는 인코딩은 다르지만, ASCII 문자열을 비교했기 때문
# (ASCII 문자값은 인코딩이 달라도 내부값은 같다)
print((b'python') == 'python'.encode('euc-kr')) # True

# 당연히 아래는 다르다, b'파이썬' 하면 에러나기 때문에 '파이썬'.encode() 로 비교
# (ASCII 아닌 문자값은 인코딩이 다르면 내부값도 다르다)
print('파이썬'.encode() == '파이썬'.encode('euc-kr')) # False

# bytes() 로 바이트 문자열 만들기
byte_data = bytes('파이썬','utf-8') # 'utf-8' 인수 없으면 에러
print(type(byte_data), byte_data) #<class 'bytes'> b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'
print(byte_data == '파이썬'.encode()) # True

# 문자열에 ASCII 아닌 문자열은 유니코드로 표현,ASCII 부분은 그대로 표현
print('사랑python'.encode()) # b'\xec\x82\xac\xeb\x9e\x91python'

# 인코딩/디코딩
byte_data = bytes('파이썬','utf-8')
print(byte_data) # b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'

b_str = b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'
print(b_str.decode('utf-8')) # 파이썬
# print(b_str.decode('euc-kr')) # 에러, 정확한 디코딩 형식을 지정해야함.
# UnicodeDecodeError: 'euc_kr' codec can't decode byte 0xed in position 0: illegal multibyte sequence
# decoding with 'euc-kr' codec failed

# 바이트 문자열 <=> 16진수 문자열 반환
str_data = bytes('Hello','utf-8').hex()
print(str_data) # 48656c6c6f

byte_data = bytes.fromhex('48656c6c6f') # 48656c6c6f 또는  (공백 구분자 가능=> 48 65 6c 6c 6f)
print(byte_data) # b'Hello'

str_data = bytes('Hello','utf-8').hex('-')
print(str_data) # 48-65-6c-6c-6f

# byte_data = bytes.fromhex('48-65-6c-6c-6f') # 이건 에러

# 바이트문자열.replace(b'src', b'target')
byte_data = b'abcdef'
r_byte_data = byte_data.replace(b'cd', b'CD')
print(r_byte_data) # b'abCDef'

byte_data = bytes('북쪽 korea','utf-8')
r_byte_data = byte_data.replace(bytes('북쪽','utf-8'), bytes('남쪽','utf-8'))
print(r_byte_data.decode('utf-8')) # 남쪽 korea

# 문자검색, 바이트 문자열.find(b'target') => 타켓 문자 위치 정수값 반환, 없으면 -1
byte_data = b'abcdef'
pos = byte_data.find(b'g')
print(type(pos),pos) # <class 'int'> -1

pos = byte_data.find(b'cd')
print(type(pos),pos) # <class 'int'> 2

byte_data = bytes('대한민국 korea','utf-8')
pos = byte_data.find(b'k')
print(type(pos),pos) # <class 'int'> 13 , 한글 3바이트 (0,1,2)(3,4,5)(6,7,8)(9,10,11)12,13

pos = byte_data.find(bytes('한','utf-8'))
print(type(pos),pos) # <class 'int'> 3, 한글 3바이트 (0,1,2)(3,4,5) 첫 발견 위치

# 좌우 공백제거 , 바이트 문자열.strip()
byte_data = b' abc '
print('|'+byte_data.decode() + '|') # | abc |
print('|'+byte_data.strip().decode() + '|') # |abc|

byte_data = bytes(' 한국 ','utf-8')
print('|'+byte_data.decode() + '|') # | 한국 |
print('|'+byte_data.strip().decode() + '|') # |한국|


