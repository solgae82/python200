
# 10진수 <-> 16진수
h1 = hex(97)
h2 = hex(98)
print(type(h1), h1, sep=",") # <class 'str'>,0x61, 문자열이다
print(type(h2), h2, sep=",") # <class 'str'>,0x62

print(chr(int(h1,base=16))) # a
print(chr(int(h2,base=16))) # b

print(h1 + h2) # 0x610x62

# 연산을 위해선 int로 변경해야한다
int_hap = int(h1,base=16) + int(h2,base=16)
print(type(int_hap), int_hap, sep=",") # <class 'int'>,195

hex_hap = hex(int_hap)
print(hex_hap, int(hex_hap, base=16), sep=" , ") # 0xc3 , 195

