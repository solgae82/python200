
# 자료 위치(정수) 반환하기
# 문자열 뿐만 아니라 시퀀스 자료등에 사용가능
# 문자열 전용 index() 함수도 비슷한 역할을 한다
# 값이 없을때 ValueError 예외 발생

str_data = "A lot of things occur each day! every day!"
pos = str_data.index('lot') 
print(pos) # 2
print(str_data.index('day')) # 27

# 없는 요소를 index로 찾으면 에러 
#print(str_data.index('month')) # ValueError: substring not found

if 'month' in str_data: 
    print(str_data.index('month'))
else: 
    print('month 단어 없다') # month 단어 없다

# 첫 'day' 인덱스 27 다음의 'day' 인덱스 찾기
print(str_data.index('day', str_data.index('day')+1)) # 38

# 리스트
n_list = [1,2,1]
s_num = 2
if s_num in n_list: 
    print(n_list.index(s_num)) # 1 
else:
    print(str(s_num) + ' 없다')