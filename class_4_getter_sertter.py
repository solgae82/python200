# Getter / Setter 
"""
파이썬의 @property 데코레이터는 클래스 내의 메소드를 일반 속성(필드)처럼 접근하여 사용할 수 있게 해주는 기능입니다

_age : 실제 프로퍼티명은 '_age' 으로 지어서, 외부에서 직접 접근 못하게 한다.
@property : 메소드 위에 설정되며 메소드명이 외부에서 접근하는 프로퍼티명이 된다. getter()역할로 구현한다
@age.setter : @property 로 설정한 외부접근 age 프로퍼티의 setter라는 의미. setter()역할로 구현한다.
@age.deletr : @property 로 설정한 외부접근 age 프로퍼티의 deleter라는 의미
"""
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
