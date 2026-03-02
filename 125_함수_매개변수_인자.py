"""
매개변수는 함수 정의 시 사용되는 이름(변수)이며, 인자는 함수 호출 시 전달되는 실제 값

def func(num): 
    pass
    
func(10)

위 예제에서 함수 선언에 있는 num 변수가 매개변수(parameter)
호출하는 func(10) 의 '10' 값이 인자(argurment)
"""

#위치 인수 (매개변수 위치 기준)
def my_print(a , b): 
    print(f'{a} + {b} = ' + str(a + b))

my_print(1,3) # 1 + 3 = 4

#디퐅트 인수 (항상 마지막에 와야한다)
def my_print1(a, level=1): 
    print(f'{a}의 레벨: {level}')

my_print1('유비')       #유비의 레벨: 1
my_print1('장비',4)     #장비의 레벨: 4
my_print1('관우',10)    #관우의 레벨: 10


#키워드 인자 (매개변수 키워드 기준)
def my_print2(a, level): 
    print(f'{a}의 레벨: {level}')

my_print2(level=3, a='제갈량') #제갈량의 레벨: 3

#가변 인자 (*args는 가변 튜플이다)
def my_print3(title, *args): 
    print(title,args)
    for i in args: 
        print(i, end='/')

my_print3('가변인자값 출력',1,3,5,7,9)
"""
가변인자값 출력 (1, 3, 5, 7, 9)
1/3/5/7/9/
"""
print()

def my_print4(title,**kwargs):
    print(title)
    print(kwargs)

#가변 키워드 인자 (**kwargs 는 딕셔너리 이다)
my_print4('가변키워드인자',a='삼일절',b=3)
"""
가변키워드인자
{'a': '삼일절', 'b': 3}
"""

########## 혼합

def setLevel(character, level, *args): 
    print(f'장수:{character}, 레벨:{level}')
    if(len(args) > 0): 
        print(f'가변 인자:{args}')

setLevel('조조',3) # 장수:조조, 레벨:3

setLevel('유비',3,'유명한놈','leader')
"""
장수:유비, 레벨:3
가변 인자:('유명한놈', 'leader')
"""

def setLevel2(character, level, **kwargs): 
    print(f'장수:{character}, 레벨:{level}')
    if(len(kwargs) > 0): 
        for k,v in kwargs.items(): 
            print(f'{k}:{v}')

setLevel2('조조', 3) # 장수:조조, 레벨:3

setLevel2('관우', 10, category='싸움 神', position='hero')
"""
장수:관우, 레벨:10
category:싸움 神
position:hero
"""

