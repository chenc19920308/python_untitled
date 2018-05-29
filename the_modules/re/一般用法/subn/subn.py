# 返回替换次数
# 格式：   subn(pattern, repl, string, count=0, flags=0)

import re
print(re.subn('[1-2]','A','123456abcdef'))
print(re.sub("g.t","have",'I get A,  I got B ,I gut C'))
print(re.subn("g.t","have",'I get A,  I got B ,I gut C'))


# 执行结果如下：
# ('AA3456abcdef', 2)
# I have A,  I have B ,I have C
# ('I have A,  I have B ,I have C', 3)


