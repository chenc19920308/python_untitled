import re
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).start())    #0
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).end())      #9
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).span())     #(0,9)
### group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。###
# 注：match和search 一旦匹配成功，就是一个match object对象，而match object对象有以下方法：
#   group() 返回被 RE 匹配的字符串
#   start() 返回匹配开始的位置(与指针有关，上述匹配符合的是字符串长度是 9 ,也就是从 0 开始）
#   end() 返回匹配结束的位置(与指针有关，上述匹配符合的是字符串长度是 9 ,也就是以9 结束）
#   span() 返回一个元组包含匹配 (开始,结束) 的位置 (与指针有关，上述匹配符合的是字符串长度是 9 ,也就是（0,9））
# group（）返回re整体匹配的字符串，
# group (n,m) 返回组号为n，m所匹配的字符串，如果组号不存在，则返回indexError异常