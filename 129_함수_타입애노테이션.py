#함수 매개변수와 리턴값에 타입애노테이션으로 자료형을 명시할 수 있다(강제사항은 아니다)

def setLevel(character: str, level: int) -> dict[str,int]:
    return {character:level}

dicData = setLevel('하늘', 1)
print(dicData) # {'하늘': 1}



# 글로벌 변수 사용, 함수 선언 뒤에 있어도 함수 내부에서 접근 가능
def setLevel2(character: str , level: int ) -> None:
    global greats
    greats[character] = level
    return

greats = {'유비':5, '관우': 20, '장비': 10}
setLevel2('유비',3)
print(greats) # {'유비': 3, '관우': 20, '장비': 10}

