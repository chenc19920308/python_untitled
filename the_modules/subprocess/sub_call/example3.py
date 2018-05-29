import subprocess

print("3. ################## subprocess.check_output ##############")
res1 = subprocess.call(['dir'],shell=True)
res2 = subprocess.check_call(['dir'],shell=True)
res3 = subprocess.check_output(['dir'],shell=True)
print("call结果：",res1)
print("check_call结果：",res2)
print("check_output结果：\n",res3)

# 父进程等待子进程执行命令，返回子进程向标准输出发送输出运行结果，
# 检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，
# 该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try…except…来检查。