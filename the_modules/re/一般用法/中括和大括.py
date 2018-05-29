# f = open("wenjian.txt",'r',encoding="utf")
# phones = []
# for line in f:
#     name,city,height,weight,phone = line.split()
#     if phone.startswith('1') and len(phone) == 11:
#         phones.append(phone)
# print(phones)

import re
f = open("wenjian.txt",'r',encoding="utf")
data = f.read()
phones = re.findall("[0-9]{11}",data)
print(phones)