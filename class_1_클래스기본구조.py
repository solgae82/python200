
# 클래스 기본 구조
class User: 

    # 생성자 , self(자바의 this와 동일)
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    # 첫번째 매개변수로 반드시 self 넣어줘야 함.
    def introduce(self): 
        return f'이름은 \'{self.name}\' / 나이는 {self.age}살 입니다'
    
u = User("kim", 30)
print(u.introduce()) # 이름은 'kim' / 나이는 30살 입니다
