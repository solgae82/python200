population = {'서울':100, '대전':45}
new_dict = {'대전':55, '부산':50}
# population.update(new_dict) # population |= new_dict 와 같다
population |= new_dict
print(population) # {'서울': 100, '대전': 55, '부산': 50}

d = {"boy": "소년"} # 예제
#d['boy2'] = '소녀'
#d.update(boy='소녀',{'boy2':'소년'})
d.update({'boy1':'소년'})
#d.setdefault('boy','소녀')
print(d)