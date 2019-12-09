


def get_money_from_ATM(bank_id,passwd,money):
    #验证你的银行卡是否有效
    if bank_id == "123":
    #检测：密码是否正确
        if passwd =="456":
    #取款 金额 是否 < 你的存款
            if int(money) <= 100:
    #以上符合的情况，吐出人民币给你
                print("取出"+money+"元")
                print("请拿回卡片")

            else:
                print("存款余额不足")
        else:
            print("密码不正确")
    else:
        print("卡号不正确")
    #返回值
    return bank_id, money


a = input("请插入银行卡")
b = input("请输入密码")
c = input("请输入取款金额")

r =  get_money_from_ATM(a,b,c)
print(r)
