# 클래스 메서드 / static(정적) 메서드 미리 보기
# (@classmethod/@staticmethod 데코레이터로 구현)
class User:

    @classmethod
    def create_default(cls): #클래스 전달
        return cls("default")

    @staticmethod
    def hello(): # self 인자 없다
        return "hello"
    
"""
| Java           | Python        |
| -------------- | ------------- |
| static method  | @staticmethod |
| static factory | @classmethod  |

"""

#-------- 1. 일반 메서드(객체) 
class User:
    def hello(self): # 반드시 첫 인수를 'self' 넣어 선언해야한다.
        print(self)

u = User()
u.hello() # <__main__.User object at 0x000001CE810D5B20>
"""
내부적으로: 
User.hello(u)
"""

#-------- 2. 클래스 메서드 (클래스 자신)
class User:
    count = 1

    @classmethod
    def show_count(cls): #첫 인수는 호출된 클래스(자신) 
        print(cls.count) #클래스 변수 접근 가능

User.show_count() # 1
"""
내부적으로
User.show_count(User)
"""

# 2-1. 클래스 메서드 , 대체 생성자 패턴
class User:
    def __init__(self, name):
        self.name = name

    @classmethod
    def guest(cls): #게스트 생성자 구현
        return cls("guest")
    
u = User.guest() # 게스트 생성자로 생성
print(u.name) # guest
"""
Java 생성자 오버로딩 같은 기능을 
Python은 이름 있는 대체 생성자 패턴 메서드로 만든다

(Python은 오버로딩 없음)

그래서:

    User.guest()
    User.from_json()
    User.from_db()

이렇게 classmethod로 분리함.
"""


#-------- 3. staticmethod(), self 필수 인자 필요없음.
# 
class User:
    @staticmethod
    def t_msg():    # self 인자 없음
        print('홍길동')
    
u = User()
u.t_msg()   # 홍길동 , (인스턴스 호출)

User.t_msg()# 홍길동 , (클래스.method로 호출)

"""
t_msg() 는
내부적으로 인스턴스,클래스 인자 없이 독립적으로 실행되는 함수가 됨.
(클래스와 관련된 실행된 함수)
그래서 t_msg(self) 로 선언하지 않아도 실행되는 것임.
"""

#-------- 요약 
"""
@classmethod = 생성 전략
@staticmethod = 클래스 관련 독립 실행되는 유틸 함수
"""