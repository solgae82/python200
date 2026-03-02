# 이름 없는 람다 함수 , lamda 키워드로 사용한다
# 람다 함수는 결과를 return 한다

fn = lambda x: x**2
print(fn(2)) # 4
print(fn(4)) # 16

txt_file = lambda name: name + '.txt'
print(txt_file('비오는 하루')) # 비오는 하루.txt

result_one = lambda x: x[1]
print(result_one('readme')) # e
print(result_one(['하이','루'])) # 루

