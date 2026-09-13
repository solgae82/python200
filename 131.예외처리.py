"""
try → 실행
except → 예외
else → 성공
finally → 무조건

ValueError       값
TypeError        타입
IndexError       인덱스
KeyError         키
AttributeError   속성
NameError        이름
FileNotFoundError 파일
ZeroDivisionError 0 나눗셈

as e   → 예외 객체
raise  → 예외 발생
"""



# 예제 1 (기본 except)
file = 'f3'
try:
    f_name = file.split('.')
    print(f'이름:{f_name[0]}, 확장자:{f_name[1]}')
except:
    print(f'에러파일=>{file}') # 에러파일=>f3

# 예제 2 (Exception)
file = 'f3'
try:
    f_name=file.split('.')
    print(f'이름:{f_name[0]}, 확장자:{f_name[1]}')
except Exception: 
    print(f'에러밣생') # 에러발생

# 예제 3 (Exception as e)
file = 'f3'
try:
    f_name=file.split('.')
    print(f'이름:{f_name[0]}, 확장자:{f_name[1]}')
except Exception as e: 
    print(f'에러=>{e}') # 에러=>list index out of range

# 예제 4 (여러 Exception)
file = 'f3'
try:
    f_name=file.split('.')
    print(f'이름:{f_name[0]}, 확장자:{f_name[1]}')
except IndexError as e: 
    print(f'IndexError=>{e}') # IndexError=>list index out of range
except Exception as e: 
    print(f'Exception=>{e}') 

# 예제 5 (else)
file_list = ['f1.jpg','f2','f3.png']
for f in file_list: 
    try:
        f_name=f.split('.')
        print(f'이름:{f_name[0]}, 확장자:{f_name[1]}')
    
    except Exception as e: 
        print(f'Exception=>{e}') 

    else:
        pass 
        print(f'안전하게 모두 실행됨') # try문 예외발생 안하면 무조건 실행ㄴㄴ

"""
이름:f1, 확장자:jpg
안전하게 모두 실행됨
Exception=>list index out of range
이름:f3, 확장자:png
안전하게 모두 실행됨
"""

# 예제 5 (filnally)
file = 'f3'
try:
    f_name=file.split('.')
    print(f'이름:{f_name[0]}, 확장자:{f_name[1]}')
except: 
    print('except=>예외발생') # except=>예외발생
else: 
    print("예외없이 실행됨")
finally: 
    print('finally=>무조건 실행') # finally=>무조건 실행

# 예제 6 (raise, 예외 강제 발생)
file = 'f3'
try: 
    if file =='f1': 
        print('정상 체크')
    else: 
        raise RuntimeError('뭔가 잘못 되었음!')
except RuntimeError as e: 
    print(f'RuntimeError=>{e}') # RuntimeError=>뭔가 잘못 되었음!
except Exception as e: 
    print(f'Exception=>{e}') 

# 예제 (보너스 예제)
data = ['a','bc',1,'de']
try:
    for d in data: 
        assert type(d) is str, f'문자열 아닌 데이터 [{d}] 있음' # 예외발생시 for문 종료
        print(d)
except AssertionError as e: 
    print(f'AssertionError=>{e}')

"""
a
bc
AssertionError=>문자열 아닌 데이터 [1] 있음
"""

###
#   try 안에 for문 예외 : 반복 종료
#   for문 안에 try 예외 : 해당 반복만 예외처리, 다음 진행
###