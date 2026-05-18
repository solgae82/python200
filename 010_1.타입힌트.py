"""
<타입힌트>

타입을 사용하면 (에러)예측 가능한 기법을 구현할 수 있다.

파이썬은 변수에 타입을 지정하지 않는 동적언어다.

파이썬에는 자료형에 애노테이션 문법으로 
타입을 알려주는 힌트 기능을 추가했다.

파이썬에서는 타입 힌트 라는 문법으로 타입체크를 할 수 있다.

타입 힌트(hint) = 타입 애노테이션 (같은 의미로 쓰인다)
(타입 애노테이션이라는 문법을 사용해 타입 힌트를 제공한다)

타입이 다르다고 해서 에러가 나거나, 
강제하지 않지만, 코딩 가독성 향샹 기법.
(대신 mypy 같은 정적 분석 도구를 사용하면 
코드를 실행하기 전에 타입 오류를 찾아준다.)

(일반 변수 타입 컨벤션)
name:str='' 보단, 
name: str = '' 로 애노테이션 전에 공백을 추가해서 사용하자.

(컬렉션 자료형 타입)
컬렉션 자료형만 지정
    
    t_list: list = ['삼국지', '수호지', '초한지']

요소 타입 지정
   
    # 자료형 지정, 요소로는 문자열만..
    str_list: list[str]  = ['삼국지', '수호지', '초한지']

    # 자료형 지정, 요소로 문자열 또는 int형만..
    t_list: list[str | int]  = ['삼국지', 1, '초한지']
    
요소 위치에 정확히 맞게 타입 설정(위치지정)

    # 리스트 자료형 [문자열,정수형,실수형] 3개 요소만 설정
    t_list: list[str,int,float] = ['삼국지', 1, 1.23]

    
※ set 자료형은 위치지정 문법을 쓸 수 없다(set은 순서 없는 자료형이므로)
    

3.12 버전과, 3.14 버전의 차이가 있다. 

(3.12 버전 기준으로 기본문법 설명하고 , 3.14 버전은 다음 장에서 설명.)
"""


"""
3.12 버전 기준
"""

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
print(__annotations__) # 전역 변수 어노테이션 확인, 3.14 버전에서는 에러(직접 접근 제한 되었다고 함.)
"""
{
    'name': <class 'str'>, 
    'age': <class 'int'>, 
    'weight': <class 'float'>, 
    'is_badman': <class 'bool'>, 
    'booklist': <class 'list'>, 
    'island': tuple[str, float, float], 
    'top4_familyname': dict[str, int]
}
"""
print('-------------')
#함수 애노테이션 체크
def example(name: str, age: int) -> str:
    return f"{name} is {age}"

print(example.__annotations__) 
# {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}

print('-------------')

