#파이썬에서는 블록'{}' 대신 들여쓰기가 블록 역할을 한다
# 탭 공백 보다는 스페이스바 4개가 표준, IDE 설정으로 탭치면 스페이스 4칸으로 설정하자
# 같은 블록내에 탭과 공백을 혼용하면 에러난다. 일관성을 지키자
# 파이썬은 공백(스페이스) 4칸이 '진리' 라고 하네
# 제어문 구분자 ':' 후 공백 한개 넣는게 컨벤션이라고 함.

listData=['a','b','c']  
#     listData=['a','b','c'] # IndentationError: unexpected indent , 에러

if 'a' in listData: #공백한개
    print('a 있다') # a 있다
    
    # 들여쓰기 간격은 모두 동일해야한다
    #   print('있응께 좋냐?') # IndentationError: unexpected indent , 에러

else: #공백한개
    print('non exist')

#아래와 같이 코딩시 구분하기 좋게 ':' 다음에 무조건 공백한개
if 'a' in listData: print('a 있당께') # a 있당께 , 



