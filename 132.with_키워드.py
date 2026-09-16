
"""
파이썬의 with 문은 자원을 획득하고 사용한 뒤 자동으로 반납(해제)해 주는 문법
with 구문을 사용하면 코드가 실행되는 동안 예외(에러)가 발생하더라도 자원을 안전하게 close(닫기) 해 준다는 강력한 장점이 있습니다

with 표현식 as 변수:
    # 자원을 사용하는 코드 블록 (코드블록예외도 예외도 with 에서 처리함)
    pass
"""


# try-finally 와 비교
f = open('컬렉션요약.txt','r',encoding='UTF-8')
try: 
    data = f.read()
finally: 
    f.close()

# with문
with open('컬렉션요약.txt','r',encoding='UTF-8') as f: 
    data = f.read()
# 코드가 이 줄로 넘어오는 순간 file은 자동으로 닫힙니다.

# 여러 자원 동시 얻기
with open("source.txt", "r") as src, open("dest.txt", "w") as dest:
    dest.write(src.read())
# 블록이 끝나면 src와 dest 파일이 모두 안전하게 닫힙니다.

# 내가 직접 만들기 (컨텍스트 매니저)
"""
__enter__와 __exit__ 메서드는 오직 with 문(컨텍스트 매니저)을 위해서만 설계된 특수한 매직 메서드
"""
class MyRoom:
    def __enter__(self):
        print("불을 켭니다.")
        return self # as 뒤의 변수로 전달될 객체

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("방을 나갈 때 불을 자동으로 끕니다.")
        # 에러가 발생했더라도 이 블록은 무조건 실행됩니다.

with MyRoom():
    print("방에서 공부를 합니다.")

""" 출력: 
불을 켭니다.
방에서 공부를 합니다.
방을 나갈 때 불을 자동으로 끕니다.
"""

"""
__exit__ 매직메서드 인수들(에러 있을 경우, 없을땐 모두 None)

    exc_type (Exception Type, 에러 이름)
    exc_val (Exception Value, 에러 내용)
    exc_tb (Exception Traceback, 에러 지도)

    return True / False
       return 없거나 False: 발생한 에러를 파이썬이 그대로 화면에 시빨갛게 띄우며 프로그램을 멈춥니다. 
       True: 에러를 쓱 지워버리고 프로그램이 멈추지 않고 계속 실행되게 만듭니다. (에러 흡수)
"""
class SmartErrorHandler:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 에러가 안 났다면 평화롭게 통과
        if exc_type is None:
            return float('nan') # 파이썬에서 일반 리턴은 False로 취급됩니다.

        # 1. 내가 대처할 수 있는 에러들만 모아서 처리하기
        if issubclass(exc_type, (ZeroDivisionError, ValueError)):
            print(f"🩹 [자동 복구] 예상된 에러({exc_type.__name__})가 발생하여 자동 치료했습니다.")
            return True  # 이 에러들은 여기서 끝냅니다 (안전)

        # 2. 내가 모르는 에러(예: 시스템 에러, 오타 등)라면?
        print(f"🚨 [비상] 예상치 못한 심각한 에러 발생! 감당할 수 없으니 위로 던집니다.")
        return False  # ⭐ False를 리턴하면 파이썬이 원래 에러를 그대로 화면에 띄우며 멈춥니다.


with SmartErrorHandler():
    # 오타 발생! print를 prnt라고 잘못 적었습니다. (코드 블록도 예외처리 대상)
    prnt("안녕하세요")  # <- NameError 발생!

"""
🚨 [비상] 예상치 못한 심각한 에러 발생! 감당할 수 없으니 위로 던집니다.
Traceback (most recent call last):
  File "d:\workspaces\python200\test.py", line 83, in <module>
    prnt("안녕하세요")  # <- NameError 발생!
    ^^^^
NameError: name 'prnt' is not defined. Did you mean: 'print'?
"""