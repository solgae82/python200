# __str__ 메서드 (java 의 toString() 느낌)

class User: 
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'User 이름:{self.name}'
    

user = User("관우")
print(user) # User 이름:관우


"""
__repr__ : 개발자용(디버깅용), eval()로 재생산 가능하게 출력 구조 잡는게 국룰 
__str__  : 사람이 보기 좋은 출력 , java의 toString() 느낌

실무에서는 둘 중 하나만 먼저 정의함.
"""