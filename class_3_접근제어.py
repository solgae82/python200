# 접근제어 (완전한 캡슐화 아님, 신뢰기반 파이썬 문화)
class User: 
    def __init__(self):
            self._name = "kim"   # protected 관례 ("건들지 마세요" 관례)
            self.__age = 30      # name mangling , 인터프리터가 _User__age 로 변경함. 상속시 덮어쓰기 막기 목적.

            