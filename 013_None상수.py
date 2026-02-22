"""
None 상수,
    None은 값의 부재, 널(null) 상태, 또는 정의되지 않은 상태를 나타내는 특수한 내장 객체(singleton)입니다. 
    주로 변수 초기화, 함수에서 반환 값이 없을 때, 혹은 기본 인자값으로 사용
    
    None 비교 (is, is not): None은 고유한 싱글톤 객체이므로 
        if x is None: 또는 if x is not None: 형태로 검사합니다.
    
    초기화 및 부재 표시: 변수를 미리 선언하거나, 찾지 못한 값을 반환할 때 사용합니다.
        result = None
    
    함수의 기본 반환값: return 문이 없거나 return만 있는 경우 자동 반환됩니다.
    
    가변(Mutable) 기본 인수: 
        리스트나 딕셔너리를 인수의 기본값으로 설정할 때 def func(a=None): 형태로 사용하여 버그를 방지합니다. 

    False , 0, "" 값과는 다르다

"""
val = None # 변수 초기화
flag = True

print(type(val)) #<class 'NoneType'>

#None 체크
if val is None: print('val 값이 없어!') # val 값이 없어!

if flag: 
    val = [1,2,3,4,5]
else: 
    val = 'Hi'

print(val) #[1, 2, 3, 4, 5]

#함수값 반환, return 이 없으면 None 반환
def no_return(): 
    pass

print(no_return()) #None

# 가변 기본 인수 (관행), 아래와 같이 기본인수에 'None' 사용한다.(안전 코딩)
# 파이썬에서는 매개변수 기본인수에 (list_obj=[]) 이렇게 쓰면 안된다. 
# 아래처럼 'None' 으로 기본인수 설정하고 내부에서 []를 생성해서 써야한다.
def add_item(item, list_obj=None):
    if list_obj is None:
        list_obj = [] # 새 리스트 생성
    list_obj.append(item)
    return list_obj

