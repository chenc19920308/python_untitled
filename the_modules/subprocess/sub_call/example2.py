import subprocess

print("2. ################## subprocess.check_call ##########")
print("check_call与call命令相同，区别是如果出错会报错")
subprocess.check_call(['dir'],shell=True)
subprocess.check_call(['abc'],shell=True)
print("call方法与check_call方法都执行并打印命令到输出终端，但是获取不到，如果想获取到结果使用check_output")
# 父进程等待子进程执行命令，返回执行命令的状态码，如果出现错误，进行报错
# 【如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try…except…来检查】