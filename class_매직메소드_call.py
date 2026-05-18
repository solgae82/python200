class Fruit:
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
    	print(f'{self.name}가 호출됨')
        
        
apple = Fruit('사과')
apple() # 사과가 호출됨

"""
파이썬의 함수명은 'function' 클래스의 객체.
함수도 실제는 객체이다
함수명+'()' 로 호출하는 것은 그 객체 내부에 __call__을 호출하는 것.
뭔가 심오하다 ㅋ
"""