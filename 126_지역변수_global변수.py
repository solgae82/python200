param = 10  #전역 변수
def func1(param): 
    print(f'param={param}')

func1(5) # param=5
print(f'param={param}') #param=10

def func2(): 
    #param = 7
    return param

print(f'함수호출=>{func2()}')   # 함수호출=>10
print(f'전역변수=>{param}')     # 전역변수=>10

def func3(): 
    param = 7
    return param

print(f'함수호출=>{func3()}')   # 함수호출=>7
print(f'전역변수=>{param}')     # 전역변수=>10

# 함수 내부에서 전역변수 사용하기
def func4(): 
    global param
    param = 30
    return param

print(f'함수호출=>{func4()}')   # 함수호출=>30
print(f'전역변수=>{param}')     # 전역변수=>30

