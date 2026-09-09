
# 시퀀스 자료에서 요소 존재하는지 체크

str_data = "A lot of things occur each day! every day!"
flag = 'lot' in str_data
print(flag) # True

if 'day' in str_data: 
    print('day 있다') # day 있다 
else: 
    print('day 없다')

# 리스트도 마찬가지
n_list =[1,2,1]
if 2 in n_list: 
    print(str(2) + ' 있다') # 2 있다
else: 
    print(str(2) + " 없다")
