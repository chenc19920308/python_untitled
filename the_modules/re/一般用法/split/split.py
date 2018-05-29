import re
print(re.split('\d+','one1two2three3four4five5'))
# 执行结果如下：
# ['one', 'two', 'three', 'four', 'five', '']  注意后面的空格
# 按照能够匹配的子串将string分割后返回列表。
# 可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。
# 格式：re.split(pattern, string[, maxsplit])     maxsplit用于指定最大分割次数，不指定将全部分割。

print(re.split('\W+', 'Words, words, words.'))
# ['Words', 'words', 'words', '']
print(re.split('(\W+)', 'Words, words, words.'))
# ['Words', ', ', 'words', ', ', 'words', '.', '']
print(re.split('\W+', 'Words, words, words.', 1))
# ['Words', 'words, words.']
print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
# ['0', '3', '9']
print(re.split('(\W+)', '...words, words...') )
# ['', '...', 'words', ', ', 'words', '...', '']
# 如果在字符串的开始或结尾就匹配，返回的list将会以空串开始或结尾。
print(re.split("a","bbb") )
# ['bbb']
# 如果字符串不能匹配，将会返回整个字符串的list。