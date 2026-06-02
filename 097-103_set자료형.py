
# 셋 자료는 집합 개념과 비슷
set_data = {'사과','배','오렌지'}
print(set_data) # {'배', '오렌지', '사과'}

# 문자열 => set 자료형 변경
set_data = set('abc')
print(set_data) # {'c', 'a', 'b'}

# 리스트 => set 자료형 변경
set_data = set([2,1,3])
print(set_data) # {1, 2, 3}

# 튜플 => set 자료형 변경
set_data = set(('사과','배','오렌지'))
print(set_data) # {'배', '사과', '오렌지'}

# 집합 연산
set1 = set('abc')
set2 = set('bcdef')

print(set1 | set2)  # {'d', 'b', 'f', 'c', 'e', 'a'} , 합집합
print(set1 & set2) # {'b', 'c'} , 교집합
print(set2 - set1) # {'e', 'f', 'd'} , 차집합
print(set1 - set2) # {a}  , 차집합
print(set1 ^ set2) # {'e', 'a', 'f', 'd'} , 여집합
print(set1 <= set2) # False , 부분집합 여부
print(set('bc') <= set('abcd')) # True , 부분집합 여부

# 요소 추가
fruits = {'사과', '배', '바나나'}
fruits.add('오렌지')
print(fruits) # {'배', '바나나', '오렌지', '사과'}
fruits.add('오렌지')
print(fruits) # {'배', '바나나', '오렌지', '사과'}

# 요소 제거
fruits.remove('사과')
print(fruits) # {'오렌지', '배', '바나나'}
# fruits.remove('딸기') # 에러 , KeyError: '딸기

# 요소 제거
fruits = {'사과', '배', '바나나','딸기'}
print(fruits) # {'오렌지', '딸기', '배', '바나나'}
fruits.discard('딸기') # {'오렌지', '배', '바나나'}
print(fruits)

fruits.discard('딸기') # 없어도 에러 안남.
print(fruits) # {'오렌지', '배', '바나나'}

# 랜덤 요소 추출
fruits = {'사과', '배', '바나나'}
f_pop = fruits.pop() # pop 후 원본에서 제거
print(f_pop, fruits) # 바나나 {'사과', '배'}

# 비어 있는 요소에 pop하면 에러
fruits = {} 
# f_pop = fruits.pop() # TypeError: pop expected at least 1 argument, got 0

# 모든 요소 삭제
fruits = {'사과', '배', '바나나','딸기'}
fruits.clear()
print(fruits) # set()