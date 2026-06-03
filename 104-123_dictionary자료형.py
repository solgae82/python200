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


# 원복 객체 참조로 items(), keys(), values() 조회

# items() => dict_items([('key','value')])
population = {'서울':100, '부산':50}
p_items = population.items() # 딕셔너리 참조로 (키,값) 리스트 튜플 객체 반환
print(type(p_items)) # <class 'dict_items'>
print(p_items) # dict_items([('서울', 100), ('부산', 50)])

for k,v in p_items: 
    print(k,'=>',v)
'''
서울 => 100
부산 => 50
'''

# 참조객체를 사용하므로 원본객체가 변경되면 즉시 반영된다.
del population['서울'] # 원본 삭제
print(population) # {'부산': 50}
print(p_items) # dict_items([('부산', 50)]) , items()객체도 변한다

# key() => dict_keys(['키값',..])
population = {'서울':100, '부산':50}
p_keys = population.keys() # 딕셔너리 참조로 키값 리스트 반환
print(type(p_keys)) # <class 'dict_keys'>
print(p_keys) # dict_keys(['서울', '부산'])

for v in p_keys: 
    print(v , end ='/') # 서울/부산/

print()

# 참조객체를 사용하므로 원본객체가 변경되면 즉시 반영된다.
del population['부산']
print(population) #{'서울': 100}
print(p_keys) # dict_keys(['서울'])

# values() => dict_values([값,..])
population = {'서울':100, '부산':50}
p_values = population.values() # 딕셔너리 참조로 값 리스트 반환
print(type(p_values)) # <class 'dict_values'>
print(p_values) # dict_values([100, 50])
print(list(p_values)) # [100, 50]

# 참조객체를 사용하므로 원본객체가 변경되면 즉시 반영된다.
del population['서울']
print(population) # {'부산': 50}
print(p_values) # dict_values([50])

# 내장함수 reversed 로 키 순서 역순 만들기
population = {'서울':100, '대전':45, '부산':50}
r_keys = reversed(population) # 키 값 기준으로 역순 반환
print(type(r_keys)) # <class 'dict_reversekeyiterator'>
print(list(r_keys)) # ['부산', '대전', '서울']

# pop()
population = {'서울':100, '대전':45, '부산':50}
# p_value = population.pop('인천') #  키 값 없으면 에러, KeyError: '인천'
# p_value = population.pop() # 인수 없으면 에러, TypeError: pop expected at least 1 argument, got 0
p_value = population.pop('서울')
print(p_value) # 100
print(population) # {'대전': 45, '부산': 50}

p_value = population.pop('인천', -1) # 해당 값이 없으면 두번째 인수값 반환
print(p_value) # -1

# popitem() => 마지막 요소 추출 튜플로 변환
population = {'서울':100, '대전':45, '부산':50}
p_item = population.popitem()
print(type(p_item),p_item) # <class 'tuple'> ('부산', 50)
print(population) # {'서울': 100, '대전': 45}

# update(dict) => 인수 딕셔너리로 원본 갱신 및 추가
population = {'서울':100, '대전':45}
new_dict = {'대전':55, '부산':50}
population.update(new_dict) # population |= new_dict 와 같다
print(population) # {'서울': 100, '대전': 55, '부산': 50}

population.update(인천=40) # 이 표현식도 가능하다, 주의사항 문자열'' 하면 안된다
#population.update('인천'=40) # SyntaxError, 문자열 ''를 하면 에러 
print(population) # {'서울': 100, '대전': 55, '부산': 50, '인천': 40}

# 새 딕셔리너리로 조합,  새로운 dictionary 생성
population = {'서울':100, '대전':45}
u_dict = {'대전':55, '부산':50}
new_dict = population | u_dict
print(new_dict) # {'서울': 100, '대전': 55, '부산': 50}

new_dict = population | {'인천': 45}
print(new_dict) # {'서울': 100, '대전': 45, '인천': 45}

population |= {'서울':1000, '울산':40} # 원본 변경, update(dict)와 같다
print(population) # {'서울': 1000, '대전': 45, '울산': 40}

# sorted 로 딕셔너리 오름차순 정렬 반환
population = {'서울':100, '대전':45, '부산':50}
new_dict = sorted(population) # 키 오름차순 정렬 리스트 반환
print(type(new_dict),new_dict) # <class 'list'> ['대전', '부산', '서울']

new_dict = sorted(population.items()) # 키 오름차순 정렬 튜플 반환
print(type(new_dict)) # <class 'list'>
print(new_dict) # [('대전', 45), ('부산', 50), ('서울', 100)]

new_dict = sorted(population.keys()) # 키 오름차순 정렬 리스트 반환
print(type(new_dict)) # <class 'list'>
print(new_dict) # ['대전', '부산', '서울']

new_dict = sorted(population.values()) # 값 오름차순 정렬 리스트 반환
print(type(new_dict)) # <class 'list'>
print(new_dict) # [45, 50, 100]

# sorted 로 딕셔너리 내림차순 정렬 반환
population = {'서울':100, '대전':45, '부산':50}
new_dict = sorted(population, reverse=True) # 키 내림차순 정렬 리스트 반환
print(type(new_dict),new_dict) # <class 'list'> ['서울', '부산', '대전']

new_dict = sorted(population.items(), reverse=True) # 키 내림차순 정렬 튜플 반환
print(type(new_dict)) # <class 'list'>
print(new_dict) # [('서울', 100), ('부산', 50), ('대전', 45)]

new_dict = sorted(population.keys(), reverse=True) # 키 내림차순 정렬 리스트 반환
print(type(new_dict)) # <class 'list'>
print(new_dict) # ['서울', '부산', '대전']

new_dict = sorted(population.values(), reverse=True) # 값 내림차순 정렬 리스트 반환
print(type(new_dict)) # <class 'list'>
print(new_dict) # [100, 50, 45]

# sorted, 람다식으로 값 기준 오름차순 정렬 튜플 반환
population = {'서울':100, '대전':45, '부산':50}
new_dict = sorted(population.items(), key=lambda x:x[1]) # [1] 값 기준으로 오름차순 정렬
print(new_dict) # [('대전', 45), ('부산', 50), ('서울', 100)]

# sorted, 람다식으로 값 기준 내림차순 정렬 튜플 반환
population = {'서울':100, '대전':45, '부산':50}
new_dict = sorted(population.items(), key=lambda x:x[1], reverse=True) # [1] 값 기준으로 내림차순정렬
print(new_dict) # [('서울', 100), ('부산', 50), ('대전', 45)]

