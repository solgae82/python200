a = 'A' #
b = 'B'

and_op = ord(a) & ord(b) # & 비트 연산

print(ord(a), bin(ord(a))) # 65 , 0b10000001
print(ord(b), bin(ord(b))) # 66 , 0b10000010
print(and_op, bin(and_op)) # 64 , 0b10000000


bit1 = 0x61 
bit2 = 0x62 

print(bin(bit1))        # 0b1100001
print(bin(bit2))        # 0b1100010

print(bin(bit1 & bit2), (bit1 & bit2), sep=" , ")   # 0b1100000 , 96
print(bin(bit1 | bit2), (bit1 | bit2), sep=" , ")   # 0b1100011 , 99
print(bin(bit1 ^ bit2), (bit1 ^ bit2), sep=" , ")   # 0b11 , 3
print(bin(bit1 >> 1), (bit1 >> 1), sep=" , ")       # 0b110000 , 48
print(bin(bit1 << 2), (bit1 << 2), sep=" , ")       # 0b110000100 , 388

print(hex(388)) # 0x184

print(hex(179,)) # 0xb3
bit3 = 0xb3
print(bin(bit3))                                # 0b10110011
print(bin(bit3 >> 1), (bit3 >> 1), sep=" , ")   # 0b1011001 , 89


## 1바이트 데이터에서 상위 4비트, 상위 4비트 추출
byte1 = 0x6b

#하위 4비트 추출
lower_4bits = byte1 & 0x0f
print(lower_4bits, bin(lower_4bits) , sep=" , ") # 11 , 0b1011

#상위 4비트 추출
upper_4bits = (byte1 >> 4) & 0x0f
print(upper_4bits , bin(upper_4bits), sep=" , ") # 6 , 0b110