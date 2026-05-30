
ret = round(42.195)
print(type(ret), ret , sep=",") # <class 'int'>,42

ret = round(42.195, 0)
print(type(ret), ret , sep=",") # <class 'float'>,42.0

ret = round(42.195, 1)
print(type(ret), ret , sep=",") # <class 'float'>,42.2

ret = round(42.195, 2)
print(type(ret), ret , sep=",") # <class 'float'>,42.2

ret = round(42.185, 2)
print(type(ret), ret , sep=",") # <class 'float'>,42.19

ret = round(42.184, 2)
print(type(ret), ret , sep=",") # <class 'float'>,42.18

ret = round(42.195, 3)
print(type(ret), ret , sep=",") # <class 'float'>,42.195

ret = round(42.195, -1)
print(type(ret), ret , sep=",") # <class 'float'>,40.0
