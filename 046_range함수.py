
# 0~4 까지 range
int_range = range(5)
print(type(int_range), int_range) # <class 'range'> range(0, 5)
print(list(int_range)) # [0, 1, 2, 3, 4]

# 1~4 까지 range
int_range = range(1,5)
print(list(int_range)) # [1, 2, 3, 4]

# 1~9 까지, +3 간격으로 range
int_range = range(1,10,3)
print(list(int_range)) # [1, 4, 7]

# range 도 iterable이다(반복 가능)
int_list = [x for x in range(0,11,2)]
print(int_list) # [0, 2, 4, 6, 8, 10]