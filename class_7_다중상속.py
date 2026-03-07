class A: pass
class B: pass
class C(A, B): pass

"""
✔ 가능
✔ MRO(Method Resolution Order) 이해 필요

Java 개발자라면 “신중히 사용” 추천
"""

#-------- 기본 
class A: 
    def hello(self): 
        print("A hello")

class B: 
    def bye(self): 
        print("B bye")

class C(A,B): 
    pass

c = C()
c.hello() # A hello
c.bye() # B bye

#-------- MRO(Method Resolution Order) 이해
class A: 
    def hello(self): 
        print("A hello")

class B: 
    def hello(self): 
        print("B bye")

class C(A,B): 
    pass
 
c = C()
c.hello() # A hello

"""
왜 A가 나오냐?

앞에서부터 탐색하기 때문. class C(A, B) : A -> B
즉 먼저 찾은 메서드 사용
이 순서를 'MRO(Method Resolution Order)' 라고 함

"""
# 다중 클래스 탐색 순서 보기
print(C.__mro__) #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

#-------- super() 사용
class A:
    def hello(self):
        print("A")

class B:
    def hello(self):
        print("B")

class C(A, B):
    def hello(self):
        super().hello()

c = C()
c.hello() # A

# 실무에서 많이 쓰는 안전 패턴
class A:
    def hello(self):
        print("A start")
        super().hello()

class B:
    def hello(self):
        print("B start")
        super().hello()

class Base:
    def hello(self):
        print("Base")

class C(A, B, Base):
    pass

c = C()
c.hello()
"""
C → A → B → Base

출력: 
A start
B start
Base
"""

#요약
"""
다중 상속은 가능하지만,
“복잡한 계층” 만들려고 쓰면 위험하다.
"""