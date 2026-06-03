# 파이썬 3.7 부터 딕셔너리도 순서가 있다. 순서대로 출력할 뿐이다.
# 그러나 시퀀스 자료형은 아니기에, 정렬할 수 없고, 인덱스로 접근은 불가하다

# 딕셔너리 생성
population = {'서울':100, '부산':50, '인천':40}
print(population) # {'서울': 100, '부산': 50, '인천': 40}

population = dict(서울=100,부산=50,인천=41)
print(population) # {'서울': 100, '부산': 50, '인천': 41}

population = dict([('서울',100),('인천',45),('부산',50)])
print(population) # {'서울': 100, '인천': 45, '부산': 50}

# 값 추출
population = {'서울':100, '부산':50, '인천':40}
print(population['서울']) # 100
print(population.get('부산')) # 50

# print(population['대전']) # KeyError: '대전' , 없는 값 접근시 에러
print(population.get('대전')) # None

# 값 추가
population = {'서울':100, '부산':50}
population['대전']=60
print(population) # {'서울': 100, '부산': 50, '대전': 60}

population.setdefault('광주') # 값 셋팅하지 않으면 None
print(population) # {'서울': 100, '부산': 50, '대전': 60, '광주': None}

population.setdefault('울산',30)
print(population) # {'서울': 100, '부산': 50, '대전': 60, '광주': None, '울산': 30}

population.setdefault('울산') # 있는 값이면 set하지 않는다
print(population) # {'서울': 100, '부산': 50, '대전': 60, '광주': None, '울산': 30}

# 값 수정
population['광주']=45
print(population) # {'서울': 100, '부산': 50, '대전': 60, '광주': 45, '울산': 30}

# 요소값 제거
population = {'서울':100, '부산':50}
del population['부산']
print(population) # {'서울': 100}
# del population['인천'] # KeyError: '인천', 없는 값 제거하려고 하면 에러

# 값 모두 제거
population.clear()
print(population) # {}

# 딕셔너리 메모리 제거
del population
#print(population) # 없는 변수를 접근하므로 에러, NameError: name 'population' is not defined

# 키값 체크
population = {'서울':100, '부산':50}
if '서울' in population: 
    print('서울 있음') # 서울 있음

if '인천' not in population: 
    print('인천 없음') # 인천 없음


# 키값 이터레이션 생성
population = {'서울':100, '부산':50}
iter_key = iter(population)
for key in iter_key: 
    print(key, end='/') # 서울/부산/

print()
for item in population: # 기본 키값 이터레이션 반환 
    print(item , end = '/') # 서울/부산/

print()

# 복제
population = {'서울':100, '부산':50}
p = population.copy()
del p['서울']
print(population) # {'서울': 100, '부산': 50}
print(p) # {'부산': 50}

# items() => dict_items([('key','value')])
population = {'서울':100, '부산':50}
p_items = population.items()
print(type(p_items)) # <class 'dict_items'>
print(p_items) # dict_items([('서울', 100), ('부산', 50)])

for k,v in p_items: 
    print(k,'=>',v)
'''
서울 => 100
부산 => 50
'''

# items() 객체와 원본 객체는 서로 연관 반영 된다.
del population['서울'] # 원본 삭제
print(population) # {'부산': 50}
print(p_items) # dict_items([('부산', 50)]) , items()객체도 변한다

# key() => dict_keys(['키값',..])

population = {'서울':100, '부산':50}
p_keys = population.keys()
print(type(p_keys)) # <class 'dict_keys'>
print(p_keys) # dict_keys(['서울', '부산'])

for v in p_keys: 
    print(v , end ='/') # 서울/부산/

print()

# keys() 객체와 원본 객체는 서로 연관 반영 된다.
del population['부산']
print(population) #{'서울': 100}
print(p_keys) # dict_keys(['서울'])


