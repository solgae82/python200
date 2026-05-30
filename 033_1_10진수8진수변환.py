# 10진수 <-> 2진수 변환

o1 = oct(97)
o2 = oct(98)

print(type(o1),o1, sep=",") # <class 'str'>,0o141 , 문자열 리턴
print(type(o2),o2, sep=",") # <class 'str'>,0o142

print(chr(int(o1,base=8))) # a
print(chr(int(o2,base=8))) # b

print(o1 + o2) # 0o1410o142

# 연산을 위해선 int로 변경해야한다
int_hap = int(o1,base=8) + int(o2,base=8)
print(type(int_hap), int_hap, sep=",") # <class 'int'>,195

oct_hap = oct(int_hap)
print(oct_hap, int(oct_hap, base=8), sep=" , ") # 0o303 , 195