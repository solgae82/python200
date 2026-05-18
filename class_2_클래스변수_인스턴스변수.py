# 클래스 변수 vs 인스턴스 변수
class User: 
    company = "스토리"
    def __init__(self, c):
        self.company=c

u = User('이야기')
print(u.company)    # 이야기 (인스턴스 변수)
print(User.company) # 스토리 (클래스 변수)