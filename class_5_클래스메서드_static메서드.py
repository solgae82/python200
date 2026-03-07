# 클래스 메서드 / static 메서드
class User:

    @classmethod
    def create_default(cls): #클래스 전달
        return cls("default")

    @staticmethod
    def hello(): # 아무것도 전달하지 않는다
        return "hello"
    
"""
| Java           | Python        |
| -------------- | ------------- |
| static method  | @staticmethod |
| static factory | @classmethod  |

"""

#-------- 1. 일반 메서드(객체) 
class User:
    def hello(self):
        print(self)

u = User()
u.hello() # <__main__.User object at 0x000001CE810D5B20>
"""
내부적으로: 
User.hello(u)
"""

#-------- 2. 클래스 메서드 (클래스 자체)
class User:
    count = 1

    @classmethod
    def show_count(cls):
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
    def guest(cls):
        return cls("guest")
    
u = User.guest()
print(u.name) # guest
"""
Java 생성자 오버로딩 대신
Python은 이름 있는 대체 생성자 패턴 메서드를 만든다

Python은 오버로딩 없음.

그래서:

    User.guest()
    User.from_json()
    User.from_db()

이렇게 classmethod로 분리함.
"""


#-------- 3. staticmethod = 아무것도 안 받음
class User:
    @staticmethod
    def add(a, b):
        return a + b
    
sum = User.add(1,2)
print(sum) # 3
"""
내부적으로 그냥 함수 , 클래스와 관련된 함수
"""

#-------- 요약 
"""
classmethod = 생성 전략
staticmethod = 관련 유틸 함수
"""