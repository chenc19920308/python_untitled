import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '-', text))
# 执行结果如下：  JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...
# 其中第二个函数是替换后的字符串；本例中为'-'  第四个参数指替换个数。默认为0，表示每个匹配项都替换。

# 使用re替换string中每一个匹配的子串后返回替换后的字符串。
# 格式：  re.sub(pattern, repl, string, count)

# re.sub还允许使用函数对匹配项的替换进行复杂的处理。
# 如：re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)；将字符串中的空格' '替换为'[ ]'

print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', text,0))
# 执行结果如下：   JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...