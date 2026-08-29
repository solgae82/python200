
# 전체 문자열에서 특정 문자, 또는 문자열 갯수 반환
# 인수 없이 호출하면 에러 

lyrics = "A lot of things occur each day! every day!"
print(len(lyrics)) # 42
print(lyrics.count(" ")) # 8
print(lyrics.count("o")) # 3
print(lyrics.count("day")) # 2
# lyrics.count() # TypeError: count() takes at least 1 argument (0 given)

n_list = [1,2,1]
print(n_list.count(1)) # 2

