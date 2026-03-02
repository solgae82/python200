# return 의 자료형 제한은 없다
# return 만 있을 경우 None 객체 반환
# return 없으면 'return' 한 것으로 간주 

def reverse(*args): 
    result = []
    idx = len(args) - 1
    while idx >= 0:
        result.append(args[idx])
        idx -= 1

    return result

ret = reverse('가','나','다','라')
print(ret) # ['라', '다', '나', '가']

