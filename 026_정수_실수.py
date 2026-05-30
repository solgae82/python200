########
# 정수형
########
# 파이썬에서는 정수형 최대,최소값은 메모리 허용 범위까지

hexData = 0x14      # 16진법, 20(10)
intData = 20        # 10진법, 20(10)
octData = 0o24      # 8진법,  20(10)
binData = 0b10100   # 2진법,  20(10)

print(bin(intData),oct(intData),int(intData),hex(intData)) #0b10100 0o24 20 0x14


########
# 실수형
########
# 파이썬에서는 실수는 부동소수점(Foating-point) 방식을 사용
# 유효자리는 15자리 

pi = 3.14
negative_num = -2.5

# 나눗셈 결과는 언제나 실수형(float)
div = 10 / 2 
print(type(div)) # <class 'float'>

# 지수 표기법을 표현했을 경우 실수가 된다
# 지수 표기법 (e 뒤의 숫자만큼 10의 거듭제곱을 곱함)
large_num = 1.2e3   # 1200.0 (1.2 * 10^3)
small_num = 4.5e-2  # 0.045 (4.5 * 10^-2)
print(type(large_num)) # <class 'float'>

val = float('3.14')
print(type(val))    # <class 'float'>

# 컴퓨터는 2진수를 기반으로 소수를 표현하기 때문에, 
# 10진수 소수를 완벽하게 저장하지 못해 미세한 연산 오차가 발생할 수 있다.
x = 0.1 + 0.2
print(x)       # 0.30000000000000004
print(repr(x)) # 0.30000000000000004