#元组
aList = [123,'123',234.213,['index','list']]
print(aList[0],aList[0:2],aList[3])
print(aList[3][1])

aList[0] = 321
print(aList)

#字典
dict_A = {}
dict_asd = {"name":"asd","sex":"male","city":"hangzhou"}
print(dict_asd)

print(dict_asd["name"])

dict_asd["name"]= "abc"

print(dict_asd["name"])

dict_asd["city"]=["hangzhou","guilin"]
#删除
del dict_asd["sex"]


print(dict_asd)