
#--------- 1. 클래스 기본 구조
class User: 

    # 생성자 , self(자바의 this와 동일)
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    # 첫번째 매개변수로 반드시 self 넣어줘야 함.
    def introduce(self): 
        return f'이름은 \'{self.name}\' / 나이는 {self.age}살 입니다'
    
u = User("kim", 30)
print(u.introduce()) # 이름은 'kim' / 나이는 30살 입니다


#--------- 2. 클래스 변수 vs 인스턴스 변수
class User: 
    company = "지오스토리"
    def __init__(self):
        pass

    def intro(self): 
        return 'Hi'

u = User()
print(u.intro()) # Hi  (인스턴스 변수)
print(User.company) # 지오스토리 (클래스 변수)


#--------- 3. 접근제어 (완전한 캡슐화 아님, 신뢰기반 파이썬 문화)
class User: 
    def __init__(self):
            self._name = "kim"   # protected 관례 ("건들지 마세요" 관례)
            self.__age = 30      # name mangling , 인터프리터가 _User__age 로 변경함. 상속시 덮어쓰기 막기 목적.


#--------- 4. Getter / Setter 
class Person:
    def __init__(self, age):
        self._age = age  

    @property
    def age(self):
        print('age(self) 호출')
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        self._age = value

    @age.deleter
    def age(self): 
        print('_age=None 됨')
        self._age = None

p = Person(20)

# @property 호출, getter 역할
# print(p.age()) , 에러
print(p.age) # 20, 내부 '_age' 값 호출

# @age.setter 사용
# p.age(30) , 에러
p.age = 30  # OK ,
# p.age = -5  # ValueError 발생

#age.deleter 호출
del p.age # _age=None 됨
print(type(p._age)) #<class 'NoneType'>


#--------- 5. 클래스 메서드 / static 메서드
class User:

    @classmethod
    def create_default(cls):
        return cls("default")

    @staticmethod
    def hello():
        return "hello"
    
"""
| Java           | Python        |
| -------------- | ------------- |
| static method  | @staticmethod |
| static factory | @classmethod  |

"""


#--------- 6. 상속
class Person:
    def greet(self):
        return "Hello"

class User(Person):
    def greet(self):
        return super().greet() + " User"
    
u = User()
print(u.greet())  # Hello User

"""
✔ extends 없음
✔ super() 동일
"""


#--------- 7. 다중 상속 (주의)
class A: pass
class B: pass
class C(A, B): pass

"""
✔ 가능
✔ MRO(Method Resolution Order) 이해 필요

Java 개발자라면 “신중히 사용” 추천
"""
