
sopping_account_list = [
    {"name":"122","sex":"male","city":"hangzhou","age":20},
    {"name":"123","sex":"male","city":"hangzhou","age":23},
    {"name":"124","sex":"famale","city":"hangzhou","age":20},
    {"name":"125","sex":"famale","city":"hangzhou","age":21},
    {"name":"126","sex":"male","city":"hangzhou","age":20}
]

sopping_list = {"name":"122","sex":"male","city":"hangzhou","age":20}


n=0
while n !=len(sopping_account_list):
    ones = sopping_account_list[n]
    if  ones["name"] == "126":
         print(sopping_account_list[n])
         n += 1
    else:
        n += 1
#for 循环会遍历一遍列表内的元素
for one in sopping_account_list:
    if one["name"] == "126":
        print(one)
    else:
        pass

for index in range(0,len(sopping_account_list)):
    person = sopping_account_list[index]
    if person["name"] == "126":
        print(one)
    else:
        pass

#key 可以获取list键名
for key in sopping_list.keys():
    print(sopping_list[key])


for key,vavle in sopping_list.items():
    print(key,vavle)