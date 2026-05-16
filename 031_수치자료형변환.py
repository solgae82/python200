
# 정수형 변환

intData = int(1234.5)
print(type(intData), intData,sep=',') # <class 'int'>,1234

intData = int("12345")
print(type(intData), intData,sep=',') # <class 'int'>,12345

# intData = int("12345.5") # ValueError, 문자열은 숫자만 변환 가능('.'때문에 에러)
intData = int(float("12345.5")) # 실수형 만들어서 가능
print(type(intData), intData,sep=',') # <class 'int'>,12345

intData = int(0b1101)
print(type(intData), intData,sep=',') # <class 'int'>,13

intData = int('0b1101', base=2)
print(type(intData), intData,sep=',') # <class 'int'>,13

intData = int('1101', base=2)
print(type(intData), intData,sep=',') # <class 'int'>,13

intData = int(0xAF)
print(type(intData), intData,sep=',') # <class 'int'>,175

intData = int('0xAF', base=16)
print(type(intData), intData,sep=',') # <class 'int'>,175

intData = int('AF', base=16)
print(type(intData), intData,sep=',') # <class 'int'>,175


# 실수형 변환

floatData = float("123")
print(type(floatData), floatData,sep=',') # <class 'float'>,123.0

floatData = float(123)
print(type(floatData), floatData,sep=',') # <class 'float'>,123.0

floatData = float("123.4")
print(type(floatData), floatData,sep=',') # <class 'float'>,123.4

floatData = float("2E5")
print(type(floatData), floatData,sep=',') # <class 'float'>,200000.0

floatData = float(2e-3)
print(type(floatData), floatData,sep=',') # <class 'float'>,0.002


# 수치 자료 > 문자열 변환

strData = str(123)
print(type(strData), strData,sep=',') # <class 'str'>,123

strData = str(123.4)
print(type(strData), strData,sep=',') # <class 'str'>,123.4

strData = str(3e-4)
print(type(strData), strData,sep=',') # <class 'str'>,0.0003

strData = str(3e4)
print(type(strData), strData,sep=',') # <class 'str'>,30000.0
