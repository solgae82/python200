# __eq__ : 기본 객체주소 비교, java의 equals() 느낌

class User: 
    def __init__(self , name):
        self.name = name
    
u1 =User("Kim")
u2 =User("Kim")
print(u1==u2) # False

# __eq__ 정의
class User1: 
    def __init__(self , name):
        self.name = name
    
    def __eq__(self, value):
        return self.name == value.name


u1 =User1("Kim")
u2 =User1("Kim")
print(u1==u2) # True , 자동으로 u1.__eq__(u2) 호출함 

