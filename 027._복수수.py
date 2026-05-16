# 실수부 + 허수부 (모두 부동소숫점 형태), 수학의 i 대신 j 사용
cData1 = 1 + 2j         # 직접할당
cData2 = complex(1,2)   # 함수사용

print(cData1 == cData2) # True

print(cData1.real) # 1.0 , 실수부
print(cData1.imag) # 2.0 , 허수부

# 켤레 복소수
compData1 = 1 - 5j
compData2 = complex(2,3)

print(compData1.conjugate()) # (1+5j)
print(compData2.conjugate()) # (2-3j)
