import re
obj = re.match('\d+', '123uu44asf')
if obj:
    print(obj.group())

# import re
# obj = re.search('\d+', 'u123uu888asf')
# if obj:
#     print(obj.group())

# import re
# obj = re.findall('\d+', 'fa123uu888asf')
# print(obj)