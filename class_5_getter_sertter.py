# Getter / Setter 
"""
파이썬의 @property 데코레이터는 
클래스 내의 메소드를 인스턴스 변수 속성(필드)처럼 
접근하여 사용할 수 있게 해주는 기능입니다

자매품으로 @변수명.setter, @변수명.deleter 가 있다.
구현 선언 후 아래처럼 접근해서 사용할 수 있다.

num = p.age # @property age(self) 메소드 실행.
p.age = 30  # @age.setter age(self,30) 메소드 실행.
del p.age   # @age.deleter age(self) 메소드가 실행.

인스턴스 변수를 호출/셋/삭제 하는 것 같지만,
내부적으로는 메소드 호출

_age : 
    실제 프로퍼티명은 '_age' 으로 지어서, 외부에서 직접 접근 못하게 한다.
    (관례 protected 느낌)

@property : 
    메소드 위에 설정되며 메소드명이 외부에서 접근하는 프로퍼티명이 된다. 
    getter()역할

        num = p.age 
        # @property로 데코레이터된 age() 메소드 호출

@age.setter : 
    실제 변수명 _age에서 '_'를 뺀 이름으로 데코레이터 선언
    @property 로 설정한 외부접근 age 프로퍼티의 setter라는 의미. 
    setter()역할
        
        p.age = 30 
        @age.setter 로 데코레이터된 age(30) 메소드에 셋팅

@age.deleter : 
    실제 변수명 _age 에서 '_'를 뺀 이름으로 데코레이터 선언
    @property 로 설정한 외부접근 age 프로퍼티의 deleter라는 의미

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

# @property 메소드 호출, getter 역할
# print(p.age()) , 이렇게 호출하면  에러
print(p.age) # 20, 내부 '_age' 값 호출

# @age.setter 메소드로 값 셋팅, setter 역할
# p.age(30) , 이렇게 셋팅하면 에러
p.age = 30  # OK 
# p.age = -5  # ValueError 발생

#age.deleter 호출
del p.age # _age=None 됨
print(type(p._age)) #<class 'NoneType'>
