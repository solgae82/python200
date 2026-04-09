# and , or , not

x=1; y=2
strData1 = 'Hello'; strData2 = 'python'
flag1 = x == y  #False
flag2 = x < y   #True
print(flag1, flag2) # False True

flag3 = strData1 != strData2 #True
flag4 = strData1 > strData2 #False
print(flag3 , flag4) # True False

print(flag1 and flag2) # (False and True) =  False
print(flag2 and flag3) # (True and True) = True
print(flag3 or flag4)  # (True or False) = True
print(flag1 or flag4)  # (False or False) = False

print(not flag1) # not False = True
print(not flag2) # not True = False