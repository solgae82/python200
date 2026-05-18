
# list(리스트)
list_data = [1,2,3]

# tuple(튜플)
tuple_data = (1,2,3)

# string(문자열)
string_data = 'I love'

# range 객체
range_data = range(5)
for i in range_data: print(i, end='') # 01234

# binary sequence
binary_sequence = b'I love python'

"""

시퀀스 자료형의 공통 특성
- 인덱싱: 인덱스를 통한 접근, 0부터 시작
- 슬라이싱: 특정 구간의 값을 잘라서 반환, 시작 인덱스와, 끝 인덱스로 정의
- 연결: '+' 연산자로 연결, 새로운 시퀀스 자료 반환
- 반복: '*' 연산자로 여러번 반복한 새로운 시쿼스 자료 반환
- 체크: 'in' 키워드로 시퀀스 내 특정값 체크
- 갯수: len()으로 시퀀스 자료 요소 갯수(크기)를 반환
"""