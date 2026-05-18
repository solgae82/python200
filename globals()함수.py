# 1. 전역 변수와 전연 함수를 만듭니다.
my_age = 25
my_name = "Kim"

def hello():
    pass

# 2. globals()로 전역 주머니를 털어봅니다.
all_globals = globals()

print(all_globals['my_age'])   # 출력: 25
print(all_globals['my_name'])  # 출력: Kim
print(all_globals['hello'])    # 출력: <function hello at 0x00000195F5A97740>

# 3. 현재 파일(모듈)의 전역 공간(Global Scope)에 변수, 함수, 클래스들 모두 출력
print(all_globals)
"""
{
'__name__': '__main__'
, '__doc__': None
, '__package__': None
, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001CCAEADDF30>
, '__spec__': None
, '__builtins__': <module 'builtins' (built-in)>
, '__file__': 'd:\\workspaces\\python200\\globals()함수.py'
, '__cached__': None
, 'my_age': 25
, 'my_name': 'Kim'
, 'hello': <function hello at 0x000001CCAEC47740>
, 'all_globals': {...}
}
"""