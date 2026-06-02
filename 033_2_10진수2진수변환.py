
# 10진수 <-> 2진수 변환

b1 = bin(97)
b2 = bin(98)

print(type(b1),b1, sep=",") # <class 'str'>,0b1100010 , 문자열 리턴
print(type(b2),b2, sep=",") # <class 'str'>,0b1100010

print(chr(int(b1,base=2))) # a
print(chr(int(b2,base=2))) # b

print(b1 + b2) # 0b11000010b1100010

# 연산을 위해선 int로 변경해야한다
int_hap = int(b1,base=2) + int(b2,base=2)
print(type(int_hap), int_hap, sep=",") # <class 'int'>,195

bin_hap = bin(int_hap)
print(bin_hap, int(bin_hap, base=2), sep=" , ") # 0b11000011 , 195

