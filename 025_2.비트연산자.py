a = 'A' 
b = 'B'

andChr = ord(a) & ord(b) # & 문자 비트 연산

print(chr(64), chr(65), chr(66), sep=" , ")         # @ , A , B
print(a, bin(ord(a)), ord(a), sep=" , ")            # A , 0b1000001 , 65
print(b, bin(ord(b)), ord(b), sep=" , ")            # B , 0b1000010 , 66
print(chr(andChr), bin(andChr),andChr, sep=" , ")   # @ , 0b1000000 , 64

# 비트 연산
bit1 = 0x61 
bit2 = 0x62 

print(bin(bit1), int(bit1) , sep=" , ")             # 0b1100001 , 97
print(bin(bit2), int(bit2) , sep=" , ")             # 0b1100010 , 98

print(bin(bit1 & bit2), (bit1 & bit2), sep=" , ")   # 0b1100000 , 96
print(bin(bit1 | bit2), (bit1 | bit2), sep=" , ")   # 0b1100011 , 99
print(bin(bit1 ^ bit2), (bit1 ^ bit2), sep=" , ")   # 0b11 , 3
print(bin(bit1 >> 1), (bit1 >> 1), sep=" , ")       # 0b110000 , 48
print(bin(bit1 << 2), (bit1 << 2), sep=" , ")       # 0b110000100 , 388

# shift 연산 
bit3 = 0xb3
print(int(bit3)) # 179
print(bin(bit3))                                 # 0b10110011
print(bin(bit3 >> 1), (bit3 >> 1), sep=" , ")    # 0b1011001 , 89
print(bin(bit3 >> 1), int(bit3 >> 1), sep=" , ") # 0b1011001 , 89

## 1바이트 데이터에서 상위 4비트, 상위 4비트 추출
byte1 = 0x6b

#하위 4비트 추출
lower_4bits = byte1 & 0x0f
print(lower_4bits, bin(lower_4bits) , sep=" , ") # 11 , 0b1011

#상위 4비트 추출
upper_4bits = (byte1 >> 4) & 0x0f
print(upper_4bits , bin(upper_4bits), sep=" , ") # 6 , 0b110

