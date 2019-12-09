import  time
mytimes=time.time()
print(mytimes)
print("自从1970现在过去了",int(mytimes),"秒")
seconds = int(mytimes)%60 # 秒
hours =int(mytimes) // 3600 #小时
mins= (int(mytimes)%3600)//60
#mins=(mins-seconds) // 60
days =hours//24
hours = hours%24
years =days//365
days -= ( (years*365)+ (years//4))
print("自从1970现在过去了",years,"年",days,"天",hours,"小时",mins,"分",seconds,"秒")
