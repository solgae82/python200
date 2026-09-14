
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

ls = [1,2]

v = ls.pop(0)
print(v)