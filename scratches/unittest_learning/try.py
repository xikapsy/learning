#用来引发异常

try:
    print("请输入一个整数")
    a = int(input())
    print("输入值是",a)
except:
    print("请重新输入")