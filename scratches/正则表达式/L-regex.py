#正则包
import re

text= """
Hello:
My name is shengyong pan. I graduated from medical information engineering major 
of zunyi medical college. This major is a composite major.

I started to learn the content of software testing in July, 2017, but only to
test some apps on a platform of cloud testing. Meanwhile, I learned how to use
some automation and performance software online, such as loadrunning and QTP. 
In December, I came to hangzhou to officially start software testing. Before,
I mainly engaged in unmanned retail projects, mainly hardware business and 
web management background and small program testing. Test items include. 
In the work, postman, which was used for interface testing, and Charles,
which was used for catching packages on mobile phones, were used to log 
on to the server using xshell to view logs, and to write web automation
scripts using selenium in some Python, and to conduct stress tests using jmeter.
"""


#findall 在text内查找'to'文本
result = re.findall('to',text)
#结果['to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to'] 12
print(result,len(result))

#'.'匹配除换行符 \n 之外的任何单字符
result = re.findall('a..',text)
# 通配符'..'，结果 例：abc、ab.、' a '、'a b'、'ab '
print(result,len(result))

#[]标记一个中括号表达式的开始或结束
result = re.findall('a[a-z][a-z]',text)
#['ame', 'adu', 'ate', 'ati', 'ajo']48
print(result,len(result))

#()标记一个子表达式的开始和结束位置。
result = re.findall(' (a[a-z][a-z]) ',text)
#['and', 'and', 'and', 'and', 'and', 'and', 'and'] 7
print(result,len(result))
#将结果从列表转化为集合，利用集合无重复元素的特性进行去重
print(set(result))

#{}标记限定符表达式的开始和结束位置。
result = re.findall('(a[a-z]{3})',text)
#['and', 'and', 'and', 'and', 'and', 'and', 'and'] 7
print(result,len(result))

# '*' 匹配子表达式零次或多次
result = re.findall(' *[Aa][a-z][a-z]',text)
#['ame', 'adu', 'ate', 'ati', 'ajo']48
print(result,len(result))

# '+' 匹配子表达式一次或多次
result = re.findall(' *[Aa][a-z][a-z]',text)
print(result,len(result))

# '？' 匹配子表达式一次或零次
result = re.findall(' ？[Aa][a-z][a-z]',text)
print(result,len(result))

# | 指明两项之间的一个选择
result = re.findall(' *[a][a-z][a-z] |[A][a-z][a-z] ',text)
print(result,len(result))

#添加小括号后悔结构全部保留
result = re.findall(' *([a][a-z][a-z]) |([A][a-z][a-z]) ',text)
#结果[('ame', ''), ('arn', ''), ('are', ''), ('and', ''), ('are', ''), ('and', '')]
print(result,len(result))

final_result = set()
for pair in result:
    if pair[0] not in final_result:
        final_result.add(pair[0])
    if pair[1] not in final_result:
        final_result.add(pair[1])
print(final_result)