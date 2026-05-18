
"""
__new__() 매직 메소드

객체 생성시 메모리 공간 할당하고 인스턴스 반환하는 메소드.
__init__() 보다 먼저 호출됨.

싱글톤 패턴 구현, 불변객체(Immutable object) 수정 등에 활용됨.
"""

class Myclass: 
    def __new__(cls, *args, **kwargs): 
        # 부모의 __new__호출하여 실제 객체 생성, 반환
        print("1.메모리 할당 + 인스턴스 생성")
        return super().__new__(cls)
    
    def __init__(self, value): 
        print("2.객체 생성 초기화")
        self.value = value


obj = Myclass(10)
"""
1.메모리 할당 + 인스턴스 생성
2.객체 생성 초기화
"""

#------------ 1. 싱글톤 패턴 구현

class Singleton: 
    _instance = None

    def __new__(cls): 
        if(cls._instance is None):
            cls._instance = super().__new__(cls)

        return cls._instance
    
s_obj1 = Singleton()
s_obj2 = Singleton()

print(s_obj1) # <__main__.Singleton object at 0x000001C5D71E6480> <__main__.Singleton object at 0x000001C5D71E6480>
print(s_obj2) # <__main__.Singleton object at 0x000001C5D71E6480> <__main__.Singleton object at 0x000001C5D71E6480>
print(s_obj1 == s_obj2) # True

#------------ 2. 불변객체(Immutable object) 수정
"""
tuple, str 같은 불변 객체를 상속받아 
생성 시점의 데이터를 수정하거나 제어하고 싶을 때 사용합니다. 

이미 생성된 후에는 값을 바꿀 수 없으므로 생성 과정에서 개입해야 합니다.
"""

class UpperString(str): # str 상속
    def __new__(cls, value):
        # 입력받은 값을 대문자로 변환하여 부모(str)의 __new__에 전달
        return super().__new__(cls, value.upper())

s = UpperString("hello")
print(s)  # HELLO