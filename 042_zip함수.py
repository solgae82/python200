
# 두개 이상의 반복 가능 자료를 입력 받아 같은 인덱스 요소로 만든 짝 튜플을 만들어주는 zip()함수
# zip(iterable, iterable..) => 인덱스 요소로 짝 지은 튜플 반환
# zip 객체도 이터러블, 반복가능,  list() 함수로 리스트 변환 가능

male =['수퍼맨', '이몽룡', '로미오']
female=['원더우먼','성춘향','줄리엣']
couples = zip(male, female)

print(type(couples), list(couples))
# <class 'zip'> [('수퍼맨', '원더우먼'), ('이몽룡', '성춘향'), ('로미오', '줄리엣')]

couples = zip(male, female)
for i in couples: 
    print(i)

"""
('수퍼맨', '원더우먼')
('이몽룡', '성춘향')
('로미오', '줄리엣')
"""

# 짝 지을 수 있는 요소만 튜플을 만든다
male =['수퍼맨', '이몽룡', '로미오','다키프리오',"마당쇠"]
female=['원더우먼','성춘향','줄리엣']
couples = zip(male, female)

for i in couples: 
    print(i)

"""
('수퍼맨', '원더우먼')
('이몽룡', '성춘향')
('로미오', '줄리엣')
"""

print()

# strict=True 로 자료 크기가 맞지 않으면 ValueError를 발생 시킬 수 있다
couples = zip(male, female, strict=True)

for i in couples: 
    
        print(i, '<=')

"""
('수퍼맨', '원더우먼') <=
('이몽룡', '성춘향') <=
('로미오', '줄리엣') <=
Traceback (most recent call last):
  File "d:\workspace\python200\042_zip함수.py", line 40, in <module>
    for i in couples: 
    ^^^^^^^^^^^^^^^^^
ValueError: zip() argument 2 is shorter than argument 1
"""