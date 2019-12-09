aList = [123,'123',234.213,['index','list']]
print(aList[0],aList[0:2],aList[3])
print(aList[3][1])

aList[0] = 321
print(aList)

a = 1,33.234,'13d','vsd'
print(a[0])
b = 1, #单元组需要添加‘,’
print(b[0])
b=(1,)
print(b[0])
#a[0] = sdf  元组不支持赋值
print(tuple(b))


