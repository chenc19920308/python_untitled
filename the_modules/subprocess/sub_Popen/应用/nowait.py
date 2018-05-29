
#Popen对象创建后，主程序不会自动等待子进程完成。
import subprocess
child = subprocess.Popen(['ping','-c','4','www.baidu.com'])
#child.wait()　添加子进程等待，child执行完了才会执行print
print ('hello')


#执行结果如下
# [root@localhost script]# python sub.py
# hello
# [root@localhost script]# PING www.a.shifen.com (61.135.169.125) 56(84) bytes of data.
# 64 bytes from 61.135.169.125: icmp_seq=1 ttl=55 time=2.04 ms
# 64 bytes from 61.135.169.125: icmp_seq=2 ttl=55 time=1.58 ms
# 64 bytes from 61.135.169.125: icmp_seq=3 ttl=55 time=2.22 ms
# 64 bytes from 61.135.169.125: icmp_seq=4 ttl=55 time=2.13 ms
#
# --- www.a.shifen.com ping statistics ---
# 4 packets transmitted, 4 received, 0% packet loss, time 3008ms
# rtt min/avg/max/mdev = 1.580/1.995/2.220/0.251 ms

# child.poll() # 检查子进程状态
# child.kill() # 终止子进程
# child.send_signal() # 向子进程发送信号
# child.terminate() # 终止子进程
# ps: 子进程的PID存储在child.pid