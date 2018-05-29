import subprocess

print ("################## subprocess.call ###############")
print (u"call方法调用系统命令进行执行，如果出错不报错")
subprocess.call(['dir'],shell=True)
# #父进程等待子进程执行命令，返回子进程执行命令的状态码，如果出现错误，不进行报错
# 【这里说的返回执行命令的状态码的意思是：如果我们通过一个变量 res = subprocess.call(['dir',shell=True]) 获取的执行结果，
# 我们能获取到的是子进程执行命令执行结果的状态码，即res=0/1 执行成功或者不成功，并不代表说看不到执行结果，
# 在Python的console界面中我们是能够看到命令结果的，只是获取不到。想获取执行的返回结果，请看check_output。】

# 【不进行报错解释：如果我们执行的命令在执行时，操作系统不识别，系统会返回一个错误，
# 如：abc命令不存在，这个结果会在console界面中显示出来，但是我们的Python解释器不会提示任何信息，
# 如果想让Python解释器也进行报错，请看check_call】