
# 2진수 표기('0b' 로 시작)
binData = 0b10101

print('16진수=>',hex(binData))  # 16진수=> 0x15
print('10진수',int(binData))    # 10진수 21
print('8진수=>',oct(binData))   # 8진수=> 0o25
print('2진수=>',bin(binData))   # 2진수=> 0b10101

# 8진수 표기('0o' 시작)
octData = 0o24
print('16진수=>', hex(octData)) # 16진수=> 0x14
print('10진수=>', int(octData)) # 10진수=> 20
print('8진수=>' , oct(octData)) # 8진수=> 0o24
print('2진수=>',bin(octData))   # 2진수=> 0b10100


# 10진수 표기 (숫자 리털럴)
deciData = 12
print('16진수=>',hex(deciData)) # 16진수=> 0xc
print('10진수=>',int(deciData)) # 10진수=> 12
print('8진수=>',oct(deciData))  # 8진수=> 0o14
print('2진수=>',bin(deciData))  # 2진수=> 0b1100

# 16진수 표기 
hexData = 0x9d
print('16진수=>',hex(hexData))  # 16진수=> 0x9d
print('10진수=>',int(hexData))  # 10진수=> 157
print('8진수=>',oct(hexData))   # 8진수=> 0o235
print('2진수=>',bin(hexData))   # 2진수=> 0b10011101
