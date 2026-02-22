"""
c언어의 case문과 같은 제어문

match 비교조건:
    case 상태:
    case 상태|상태|상태:
    case _: #상태가 없을때 처리
"""

status = 202
match status:
    case 200|201|202: 
        print('OK') #OK
    case 400: 
        print('Bad Request')
    case 401: 
        print('Unauthrized')
    case 403: 
        print('접근금지')
    case 404: 
        print('Not found')
    case _:
        print('기타 문제')


#point = (0,0)      # 원점좌표
#point = (1,0)      # x축 값은 1
#point = (0,2)      # y축 값은 2
point = (3, 4)      # x축=3, y축=4

match point:
    case (0.0): 
        print('원점좌표')
    case (x, 0):
        print(f'x축 값은 {x}') 
    case (0, y): 
        print(f'y축 값은 {y}')
    case (x,y):
        print(f'x축={x}, y축={y}') # x축=3, y축=4
        
