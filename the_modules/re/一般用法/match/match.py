# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。直到找到一个匹配
# 注意：当正则表达式是' ^ '开头时，match与search是相同的。
# match只有当且仅当被匹配的字符串开头就能匹配 或 从pos参数的位置开始就能匹配 时才会成功。

import re
a=re.search('[\d]',"abc33").group()
print(a)
p=re.match('[\d]',"abc33")
print(p)
b=re.findall('[\d]',"abc33")
print(b)

# 执行结果：
# 3
# None
# ['3', '3']