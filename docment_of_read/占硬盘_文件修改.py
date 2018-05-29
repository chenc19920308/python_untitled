import os
f_old = "read.txt"
f_new = "new_file.txt"
f = open(f_old,"r",encoding="utf-8")
f2 = open(f_new,"w",encoding="utf-8")

old_data = "666"
new_data = "888"
for line in f:
    if old_data in line:
        line = line.replace(old_data,new_data)
        f2.write(line)
    else:
        f2.write(line)
f.close
f2.close









