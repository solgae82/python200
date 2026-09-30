population = {'서울':100, '대전':45}
new_dict = {'대전':55, '부산':50}
# population.update(new_dict) # population |= new_dict 와 같다
population |= new_dict
print(population) # {'서울': 100, '대전': 55, '부산': 50}