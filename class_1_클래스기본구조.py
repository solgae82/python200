
# 파이썬은 
# "명시적인 것이 암시적인 것보다 낫다
# (Explicit is better than implicit)"
# 는 철학을 가집니다.

# 인스턴스 구조로 만들때는 
# 반드시 첫벗째 인자에 인스턴스 변수를 전달 받을 매개변수를 넣는다
# (코딩규약에 따라) 'self'명으로 넣는다.(다른 이름이어도 에러 아님)


# 클래스 기본 구조
class User: 

    # 생성자 , self(자바의 this 개념)
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    # 첫번째 매개변수로 반드시 self 넣어줘야 함.
    def introduce(self): 
        return f'이름은 \'{self.name}\' / 나이는 {self.age}살 입니다'
    
u = User("kim", 30)
print(u.introduce()) # 이름은 'kim' / 나이는 30살 입니다

"""
내부적으로: 

User.__init__(u,"kim", 30)
User.introduce(u) 

가 된다. 명시적으로..

자바 클래스처럼 생각하면 오해가 생긴다.
"""

class Tclass:
    def test():
        print('test')

t = Tclass()

# t.test() # 에러,파이썬 실행기가 인스턴스 인수 1개를 무조건 넣는데, 선언엔 없으므로..
# TypeError: Tclass.test() takes 0 positional arguments but 1 was given

Tclass.test() # test , 이 형식으로만 사용 가능.

"""
파이썬에서는 클래스 안에 메소드 첫벗째 인자로 self가 기본.
만약 넣지 않았다면, 클래스명.메소드로만 접근하겠다는 뜻.
(파이썬에서는 이렇게 클래스 프로그래밍 하지 않는다)
언제나 명시적으로! (self,..)
"""

"""
인스턴스/클래스 인자 없이 인수없는 test()로 선언하는 방법이 있다
@staticmethod 데코레이터로 확장 (나중에 따로 정리 할 것이다)
(클래스 기본이라기 보다는 독립 함수 느낌)
"""
class Tclass2:
    @staticmethod
    def test():
        print('test')

t = Tclass2()
t.test() # test
