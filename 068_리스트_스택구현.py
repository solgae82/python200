
my_stack = []

def put_data(data): 
    my_stack.append(data)

def pop_data(): 
    if len(my_stack) <= 0: 
        return None
    
    return my_stack.pop()


put_data('사과')
put_data([1,2,3])
put_data(3.14)

print(my_stack) # ['사과', [1, 2, 3], 3.14]

tmp = pop_data()
while tmp != None: 
    print(tmp, '/ 남은=>', my_stack)
    tmp = pop_data()

"""
3.14 / 남은=> ['사과', [1, 2, 3]]
[1, 2, 3] / 남은=> ['사과']
사과 / 남은=> []
"""
