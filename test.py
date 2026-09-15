
s = {'하루','이틀','삼일'}

s.add('사흘')
print(s) # {'사흘', '삼일', '이틀', '하루'}

v = s.remove('사흘')
print(s , v) # {'하루', '이틀', '삼일'} None

v = s.discard('삼일')
print(s, v) # {'하루', '이틀'} None

p = s.pop()
print(p, s) # 이틀 {'하루'} 또는 하루 {'이틀'}
# p = s.pop('이틀') # ! 에러, 인수 넣으면 안됨.

s.clear()
print(s) # set()

s = {'하루','이틀','삼일'}
s.update(('1','2','3'),{'k1':'이종격투기', 'pride':'2세대'},[401,402])
print(s) # {'k1', '2', '삼일', 'pride', '3', '1', '하루', '이틀', 401, 402}


# 집합 연산
set1 = set('abc')
set2 = set('bcdef')

v = set1.union(set2)
print(v) # {'d', 'a', 'c', 'e', 'b', 'f'}

v = set1.difference(set2)
print(v) #{'a'}

v = set2.difference(set1)
print(v) # {'f', 'e', 'd'}

v = set1.intersection(set2)
print(v) # {'c', 'b'}


