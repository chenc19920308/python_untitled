# 可以在Popen()建立子进程的时候改变标准输入、标准输出和标准错误，
# 并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe)，如下2个例子：

import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
print (child1.stdout.read())       #或者child1.communicate()
import subprocess
child1 = subprocess.Popen(["cat","/etc/passwd"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["grep","0:0"],stdin=child1.stdout, stdout=subprocess.PIPE)
out = child2.communicate()