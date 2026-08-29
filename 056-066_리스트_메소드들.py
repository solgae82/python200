# 요소 추가
n_list = ['태양', '지구', '목성']
n_list.append('천왕성')
print(n_list) # ['태양', '지구', '목성', '천왕성']

# 요소 변경
n_list = ['태양', '지구', '목성']
n_list[1] = '금성'
print(n_list) # ['태양', '금성', '목성']

# 요소 삭제 , remove('요소")
n_list = ['태양', '지구', '목성']
#n_list.remove() # TypeError, 기본 인자 있어야함
#n_list.remove(1) # ValueError, 없는 요소 삭제하려고 했음
n_list.remove('지구')
print(n_list) # ['태양', '목성']

# 요소 삭제
n_list = ['태양', '지구', '목성']
del n_list[1]
print(n_list) # ['태양', '목성']

# 요소 삭제, (중복 요소가 있을때는 가장 먼저 발견된 요소만 삭제)
n_list = ['태양', '지구', '목성', '지구']
n_list.remove('지구')
print(n_list) #['태양', '목성', '지구']

# 모든 요소 삭제 , clear()
n_list = ['태양', '지구', '목성']
# del n_list[:] # == n_list.clear()
n_list.clear()
print(n_list) # []

# 요소 복사, copy()
n_list = ['태양', '지구', '목성']
c_list = n_list.copy()
print(c_list) # ['태양', '지구', '목성']

# 리스트 확장 , extend()
n_list = ['태양', '지구', '목성']
c_list = ['태양', '지구', '목성']
n_list.extend(c_list)
print(n_list) # ['태양', '지구', '목성', '태양', '지구', '목성']

c_list = ['태양', '지구', '목성']
e_list = c_list + ['천왕성','해왕성','명왕성']
print(e_list) # ['태양', '지구', '목성', '천왕성', '해왕성', '명왕성']

# 요소 추가(끼워넣기), insert(인덱스, 값)
n_list = ['태양', '지구', '목성']
n_list.insert(1,'금성')
print(n_list) # ['태양', '금성', '지구', '목성']

# 요소 인덱스 반환
n_list = ['태양', '금성', '지구', '목성']
print('지구index=>', n_list.index('지구')) # 지구index=> 2

# 요소값 추출(마지막 자료 추출 후 자료구조 재조정)
n_list = ['태양', '금성', '지구', '목성']
last_pop = n_list.pop()
print(last_pop, n_list) # 목성 ['태양', '금성', '지구']

# 요소값 추출(인덱스로 추출 후 자료구조 재조정)
n_list = ['태양', '금성', '지구']
v_pop = n_list.pop(n_list.index('금성'))
print(v_pop , n_list) # 금성 ['태양', '지구']

# 요소값 추출 반환, [index], [index:], [[index:end_index]
f_list = ['사과','배','수박','참외']
print(f_list[1]) # 배
print(f_list[1:]) # ['배', '수박', '참외']
print(f_list[1:2]) # ['배']
print(f_list[1:3]) # ['배', '수박']

# 요소 역순 변환 (현재 자료구조 순서 역순 변경)
n_list = ['태양', '지구', '목성']
n_list.reverse()
print(n_list) # ['목성', '지구', '태양']

# 요소 정렬 (오름차순 정렬)
n_list = ['태양','금성', '지구', '목성']
n_list.sort() # 오름차순 정렬
print(n_list) # ['금성', '목성', '지구', '태양']

# 요소 정렬 (내림차순 정렬)
n_list = ['태양','금성', '지구', '목성']
n_list.sort(reverse=True) # 내림차순 정렬
print(n_list) # ['태양', '지구', '목성', '금성']
