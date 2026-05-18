
"""
3.14 버전 (달라진 점) 

타입 애노테이션이 즉시 평가 (Eager Evaluation)가 아닌 
지연평가(Lazy evaluation)에서 동작하게 변경됨.

"""
#######################
# 1. 3.14 버전에서 글로벌 애노테이션을 보고 싶으면 아래처럼 한다.
# print(__annotations__) # 전역 변수 어노테이션 확인, 3.14 버전에서는 에러(직접 접근 제한 되었다고 함.)
#######################

from annotationlib import get_annotations, Format
import sys # 모듈 객체를 가져오기 위해 필요합니다!

# 1. 글로벌(전역 변수) 타입 힌트 작성
user_name: str = "홍길동"
user_age: int = 30

# 2. 현재 실행 중인 파일(모듈) 객체를 '요기'에 넣어줍니다.
current_module = sys.modules[__name__]

# 3. 출력 결과 확인하기
print(get_annotations(current_module, format=Format.STRING))
"""
{'user_name': 'str', 'user_age': 'int'}
"""

#######################
# 3.14 버전에서 함수에 정의된 애노테이션을 보고 싶으면 아래처럼 한다.
#######################

from annotationlib import get_annotations, Format

# 1. 애노테이션에 해당하는 실제 객체를 딕셔너리에 담음
def func (arg: str): pass
f = get_annotations(func) # 딕셔너리로 반환
print(type(f),f) #<class 'dict'> {'arg': <class 'str'>}, 실제 str 객체

f = get_annotations(func, format=Format.VALUE) # 딕셔너리로 반환
print(type(f),f) #<class 'dict'> {'arg': <class 'str'>}, 실제 str 객체 

# 2. 글자(문자열) 그대로 보여줘!
f = get_annotations(func, format=Format.STRING) # 딕셔너리로 반환
print(type(f),f) #<class 'dict'> {'arg': 'str'} , 'str' 문자열

# 3. 아직 정의 안 된 클래스가 있어도 일단 넘어가줘! (임시 마커 처리)
# 아직 정의 된적 없는 Ghost 객체
def func(arg: Ghost): pass  

f = get_annotations(func, format=Format.FORWARDREF) # 딕셔너리로 반환
print(type(f),f)
# <class 'dict'> {'arg': ForwardRef('Ghost', owner=<function func at 0x000001FBEB535640>)}
"""
 만약 존재하지 않거나 나중에 정의될 클래스(Forward Reference)를 타입 힌트에 적어두었을 때, 
 프로그램이 멈추지 않도록 임시 마커(ForwardRef 객체)로 감싸서 보여달라는 뜻입니다. 
"""

"""
왜 저런 식으로 할까?

예를 들어 아래와 같은 함수가 있다고 하고..

def func(arg: Ghost): # Ghost라는 클래스는 코드 어디에도 없음!
    pass
    
이 상태에서 4번(Format.VALUE)을 실행하면 파이썬은 "Ghost가 뭔데!" 하면서 
에러(NameError)를 뿜어냅니다. 
프로그램이 멈추는 것이죠.

하지만 2번(Format.STRING)이나 3번(Format.FORWARDREF)으로 호출하면, 
파이썬은 에러를 내지 않고 각각 {'arg': 'Ghost'} 혹은 ForwardRef('Ghost')라는 결과물로 
안전하게 바꾸어 반환해 줍니다.

즉, "타입 정보를 다룰 때 어떤 상황에서도 에러 없이 안전하게 글자로만 뽑아 쓸지(STRING), 
아니면 위험을 감수하고서라도 진짜 클래스 객체로 가져와 쓸지(VALUE)를 
개발자가 입맛대로 고르게 해주는 문법"입니다.

"""

