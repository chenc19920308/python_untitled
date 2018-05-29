import subprocess
child = subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE)     #将标准输出定向输出到subprocess.PIPE
print (child.stdout.read())   #使用 child.communicate()  也可

#  结果如下：
#         [root@localhost script]# python sub.py
#         total 12-rw-r--r--. 1 root root  36 Jan 23 07:38 analyse.sh
#         -rw-r--r--. 1 root root 446 Jan 25 19:35 sub.py