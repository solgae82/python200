class User: 
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'이름은: {self.name}'
    
u = User("Kim")
print(u) # 이름은: Kim

"""
__init__ = 생성자 (느낌), 정확히는 초기화 메서드
핵심

__init__는 객체 생성 자체가 아니라:

    - '생성된 객체를 초기화'

실제 생성은 내부적으로 __new__
근데 실무에서는 거의 __init__만 씀.
"""
