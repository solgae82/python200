# __repr__
# 관례적으로 __repr__로 출력된 문자열을 eval('출력문자열')로 다시 똑같은 객체(튜플)를 만들 수 있게 작성하는 게 국룰.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 객체의 상태를 명확하게 보여주는 공식 표현
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)

print(p) # Person(name='Alice', age=30)
print(repr(p)) # Person(name='Alice', age=30)
list = [p]
print(list) # [Person(name='Alice', age=30)]

str = repr(p)
p2 = eval(str)

print(f'새 객체(p2): {p2}') # 새 객체(p2): Person(name='Alice', age=30)
print(f'p 와 p2는 같은 객체? {p is p2}') # p 와 p2는 같은 객체? False
print(f'p.name == p2.name 결과는? {p.name == p2.name}') # p.name == p2.name 결과는? True

"""
__repr__ : 개발자용(디버깅용), eval()로 재생산 가능하게 출력 구조 잡는게 국룰 
__str__  : 사람이 보기 좋은 출력 , java의 toString() 느낌

실무에서는 둘 중 하나만 먼저 정의함.
"""