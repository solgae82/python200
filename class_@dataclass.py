from dataclasses import dataclass

@dataclass
class User: 
    name: str
    age: int

"""
자동 생성:

✅ init
✅ repr
✅ eq

자바 롬복같은 느낌!
"""

u1 = User("kim",12)
u2 = User("kim",12)
print(u1) # User(name='kim', age=12) , 자동생성된 __repr__ 출력
print(u1 == u2) # True , (자동생성된  u1.__eq__(u2) 비교 결과)

