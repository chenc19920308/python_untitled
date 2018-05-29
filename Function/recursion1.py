# n = 10
# while True:
#     n = int(n/2)
#     print(n)
#     if n == 0:
#         break

# def trues(n):
#     n = int(n/2)
#     return n
# result = trues(10)
# result2 = trues(result)
# result3 = trues(result2)
# print( result,"\n",result2,"\n",result3)


# import sys
# sys.setrecursionlimit(100)
# def trues(n):
#     n = int(n/2)
#     print(n)
#     if n > 0:
#         trues(n)
# trues(10)

# import sys
# sys.setrecursionlimit(100)
# def trues(n):
#     n = int(n/2)
#     print(n)
#     if n > 0:
#         trues(n)
#     print(n)
# trues(10)                函数是一层一层推出的。

# def trues(n,count):
#     print(n,count)
#     if count < 5:
#         trues(n/2,count+1)
# trues(180,1)

# def trues(n,count):
#     print(n,count)
#     if count < 5:
#         trues(n/2,count+1)
#     return
#
# res = trues(180,1)
# print(res)


# def trues(n,count):
#     print(n,count)
#     if count < 5:
#         return trues(n/2,count+1)
#     else:
#         return n
# res = trues(180,1)
# print("res",res)     解决了返回值问题
