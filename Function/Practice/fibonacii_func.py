#use recursion
# def fibo(n):
#     if n < 1:
#         print("Wrong Number")
#         return -1
#     if n == 1 or n == 2:
#         return 1
#     if n > 2:
#         return fibo(n-1) + fibo(n-2)
#
# number = int(input("Number of figures:"))
# print("第%d位数值是：%d"%(number,fibo(number)))

#no recursion
# no recursion
# def fibo(n):
#     a1,a2,a3 = 1,1,1
#     if n < 1:
#         print("Wrong Number")
#         return -1
#     while (n-2) > 0:
#         a3 = a1 + a2
#         a1 = a2
#         a2 = a3
#         n -= 1
#     return a3
# number = int(input("Number of figures:"))
# print("第%d位数值是：%d"%(number,fibo(number)))