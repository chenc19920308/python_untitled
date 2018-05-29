import re
w = re.findall('\btina','tian tinaaaa')
print(w)
s = re.findall(r'\btina','tian tinaaaa')
print(s)
v = re.findall(r'\btina','tian#tinaaaa')
print(v)
a = re.findall(r'\btina\b','tian#tina@aaa')
print(a)
# \b:匹配\w和\W之间，即匹配单词边界，也就是指单词和空格间的位置。
# 例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。

# Output results
# []
# ['tina']
# ['tina']
# ['tina']