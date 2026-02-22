#파이썬은 변수에 타입을 지정하지 않는다.
#자료형에 힌트로 타입을 알려주는 애노테이션 기능
#타입이 다르다고 해서 에러가 나거나, 강제하지 않지만, 코드 가독성을 위한 코딩 기법
# name:str='' 보단, name: str = '' 로 애노테이션 전에 공백을 추가해서 사용하자.

name: str = 1
print(type(name)) #<class 'int'> , str 타입으로 지정해 놓고 실제로는 수치형을 사용했다(x), 에러나지 않는다

name: str ='하이'
print(type(name)) #<class 'str'> , 이렇게 사용하자

age: int = 17
weight: float = 70.1
is_badman: bool = False

#리스트 
booklist: list = ['삼국지', '수호지', '초한지']

#튜플
island: tuple[str, float, float] = ('독도', 131.52, 37.14)

#딕셔너리
top4_familyname: dict[str,int] = {'김씨':1, '이씨':2, '박씨':3, '나씨':4}


print('-------------')

# print(__annotations__) # 전역 변수 어노테이션 확인, 3.14 버전에서는 에러(직접 접근 제한 되었다고 함.)
print(globals())
"""
{
    '__name__': '__main__'
    , '__doc__': None
    , '__package__': None
    , '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001C92C37DF30>
    , '__spec__': None
    , '__builtins__': <module 'builtins' (built-in)>
    , '__file__': 'd:\\python200\\010_타입애노테이션.py'
    , '__cached__': None
    , '__annotate__': <function __annotate__ at 0x000001C92C4DB740>
    , '__conditional_annotations__': {0, 1, 2, 3, 4, 5, 6, 7}
    , 'name': '하이'
    , 'age': 17
    , 'weight': 70.1
    , 'is_badman': False
    , 'booklist': ['삼국지', '수호지', '초한지']
    , 'island': ('독도', 131.52, 37.14)
    , 'top4_familyname': {'김씨': 1, '이씨': 2, '박씨': 3, '나씨': 4}
} 
"""

print('-------------')
#함수 애노테이션 체크
def example(name: str, age: int) -> str:
    return f"{name} is {age}"

print(example.__annotations__) #{'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}

print('-------------')
# 3.14 버전에서는 아래와 같이 사용 , 타입 애노테이션이 정의 시점이 아닌 접근 시점(지연평가)에 동작한다고 함.
from annotationlib import get_annotations, Format
def func (arg: str): 
    pass

print(get_annotations(func)) #{'arg': <class 'str'>} , 실제 객체 반환
print(get_annotations(func, format=Format.STRING)) #{'arg': 'str'} , 문자열로 반환
print(get_annotations(func, format=Format.FORWARDREF)) #{'arg': <class 'str'>} ,정의되지 않은 이름을 특수 마커로 대체 
print(get_annotations(func, format=Format.VALUE)) #{'arg': <class 'str'>} , 기존처럼 런타임시 평가

# 이런 방법도 있다 
print('-------------')
import typing
print(typing.get_type_hints(func)) #{'arg': <class 'str'>}

