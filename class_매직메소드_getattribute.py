
# __getattribute__ 메소드 , 속성 접근 처리 전 Hooking 느낌.

class MyClass:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, acces_name):
        
        print(f"[로그] 접근한 속성 이름: {acces_name}")
        # 무한 루프를 방지하기 위해 super()를 사용해 실제 속성 값을 가져옵니다.
        return super().__getattribute__(acces_name)

obj = MyClass("파이썬")

# 속성 접근 시 __getattribute__가 먼저 호출됩니다.
print(obj.name)
"""
[로그] 접근한 속성 이름: name
파이썬
""" 

"""
주의점: 
__getattribute__ 안에서 속성을 반환하기 위해 
self.name 같은 일반적인 속성 접근 방식을 사용하면, 
그 접근 때문에 __getattribute__가 또 호출되는 
무한 재귀에 빠지게 됩니다.

따라서 반드시 super().__getattribute__(name)을 사용하거나 
object.__getattribute__(self, name)을 통해 
기본 속성 조회 기능을 사용해야 합니다.
"""