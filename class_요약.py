class User: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    def introduce(self): 
        return f'이름은 \'{self.name}\' / 나이는 {self.age}살 입니다'
    
u = User("kim", 30)
print(u.introduce())

class User: 
    company = "지오스토리"
    def __init__(self):
        pass

    def intro(self): 
        return 'Hi'

u = User()
print(u.intro()) # 인스턴스 변수
print(User.company) #클래스 변수

class User: 
    def __init__(self):
            self._name = "kim"   # protected 관례
            self.__age = 30      # name mangling , 인터프리터가 _User__age 로 변경함.

# Getter / Setter 
"""
파이썬의 @age.setter는 @property로 정의된 게터(getter) 메소드와 함께 사용하여 
클래스 속성(나이)에 값을 저장하기 전 유효성 검사 등 논리적 로직을 추가하는 캡슐화 방식입니다. 
이를 통해 p.age = -5와 같은 잘못된 데이터 입력을 제어할 수 있습니다. 

작동 방식 및 예제:
@property (getter): age 값을 읽을 때 호출. 내부적으로 _age 변수 사용.
@age.setter (setter): age 값을 변경(p.age = 20)할 때 호출되어 검증 후 _age에 할당. 

핵심 포인트:
_age (Hidden Variable): 실제 데이터는 _age에 저장하며외부에서는 age 프로퍼티를 통해 접근하도록 유도합니다.
데이터 검증: 나이 설정 시 0보다 작은 값이 들어오면 에러를 발생시켜 안전한 데이터 관리가 가능합니다.
사용 편의성: 메소드임에도 불구하고 p.age = 30과 같이 일반 필드처럼 값을 할당할 수 있습니다. 

"""
class Person:
    def __init__(self, age):
        self.age = age  # setter가 호출됨

    @property
    def age(self):
        print('age(self) 호출')
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        self._age = value

p = Person(20)
p.age = 30  # OK , age setter 사용
# p.age = -5  # ValueError 발생
print(p.age) # age()하면 에러, 
#age(self) 호출
#30

