import subprocess
child1 = subprocess.Popen(['cat','/etc/passwd'],stdout=subprocess.PIPE)
child2 = subprocess.Popen(['grep','root'],stdin=child1.stdout,stdout=subprocess.PIPE)
print (child2.communicate())

# 结果如下：
#   ('root:x:0:0:root:/root:/bin/bash\n, None)

# subprocess.PIPE实际上为文本流提供一个缓存区。
# child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走。
# child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本。
# 注意：communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成