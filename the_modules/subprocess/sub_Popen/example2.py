import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write(b'print 1 \n')
obj.stdin.write(b'print 2 \n')
obj.stdin.write(b'print 3 \n')
obj.stdin.write(b'print 4 \n')

out_error_list = obj.communicate()
print(out_error_list)