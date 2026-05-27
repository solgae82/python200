
import collections

my_queue = collections.deque()

def put_data(data): 
    my_queue.append(data)

def pop_data(): 
    if len(my_queue) <= 0: 
        return None
    
    return my_queue.popleft()

put_data('사과')
put_data([1,2,3])
put_data(3.14)

print(my_queue) # deque(['사과', [1, 2, 3], 3.14])

tmp = pop_data()
while tmp != None: 
    print(tmp , '/남은=>', my_queue)

    tmp = pop_data()

"""
사과 /남은=> deque([[1, 2, 3], 3.14])
[1, 2, 3] /남은=> deque([3.14])
3.14 /남은=> deque([])
"""
