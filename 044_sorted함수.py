# sorted(iterable) => 반복 자료 오름차순 정렬한 리스트 반환
list_data = [22,1,25,9,15]
print(sorted(list_data)) # [1, 9, 15, 22, 25]

# sorted(iterable , reverse=True) => 반복 자료 내림차순 정렬한 리스트 반환
print(sorted(list_data,reverse=True)) # [25, 22, 15, 9, 1]

tuple_data = ('사과','바나나','참외')
print(sorted(tuple_data)) # ['바나나', '사과', '참외']

# 문자열은 문자단위 정렬된 리스트 반환
str_data = 'I love python'
print(sorted(str_data)) # [' ', ' ', 'I', 'e', 'h', 'l', 'n', 'o', 'o', 'p', 't', 'v', 'y']

# 딕셔너리는 키 기준(디폴트) 정렬된 리스트 반환
population = {'박씨':1, '김씨':3, '이씨':2}
print(sorted(population)) # ['김씨', '박씨', '이씨']

# 딕셔너리 값 기준 정렬된 리스트 반환
print(sorted(population.items() , key=lambda x: x[1])) # [('박씨', 1), ('이씨', 2), ('김씨', 3)]

# 딕셔너리 값 기준 정렬된 딕셔너리 반환
print(dict(sorted(population.items() , key=lambda x: x[1]))) # {'박씨': 1, '이씨': 2, '김씨': 3}

# set 자료형 정렬된 리스트 반환
set_data = {'야구','축구','농구'}
print(sorted(set_data)) # ['농구', '야구', '축구']