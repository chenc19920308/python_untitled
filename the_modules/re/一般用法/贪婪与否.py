#  *?,+?,??,{m,n}?    前面的*,+,?，{} 等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
import re
a = re.findall(r"a(\d+?)",'a23b')
print(a)                              # ["2"]
b = re.findall(r"a(\d+)",'a23b')
print(b)                              #["23"]

a = re.match('<(.*)>','<H1>title<H1>').group()
print(a)                                #  <H1>title<H1>
b = re.match('<(.*?)>','<H1>title<H1>').group()
print(b)                                #  <H1>

a = re.findall(r"a(\d+)b",'a3333b')
print(a)                                # ['3333']
b = re.findall(r"a(\d+?)b",'a3333b')
print(b)                                # ['3333']

#  这里需要注意的是如果前后均有限定条件的时候，就不存在什么贪婪模式了，非匹配模式失效。