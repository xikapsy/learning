year = eval(input("请输入贷款年限"))
money = eval(input("请输入贷款金额"))
monthrate = eval(input("请输入贷款利率"))

monthmoney = (money*monthrate)/(1-(1/(1+monthrate)**(year*12)))
allmoney = monthmoney *12*year
print("月供",monthmoney)
print("全部还款",allmoney)