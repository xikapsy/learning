import os
cmd = input("cmd")

# if  cmd =="notepad":
#     os.system(cmd)
isrun =(cmd == "notepad") # == 逻辑判断，真假
print(isrun)
if isrun:
    os.system(cmd)
