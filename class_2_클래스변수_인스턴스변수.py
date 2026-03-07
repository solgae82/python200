# 클래스 변수 vs 인스턴스 변수
class User: 
    company = "지오스토리"
    def __init__(self):
        pass

    def intro(self): 
        return 'Hi'

u = User()
print(u.intro()) # Hi  (인스턴스 변수)
print(User.company) # 지오스토리 (클래스 변수)