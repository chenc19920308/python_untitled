i = 0
def Num():
    global i
    i = i + 1
    print('cishu', i)


def hanoi(n,x,y,z):
    if n == 1:
        print(x,"--->",z)
        Num()
        return

    else:
        i = 0
        hanoi(n-1,x,z,y)
        print(x,"--->",z)
        Num()
        hanoi(n-1,y,x,z)
n = int(input("请输入汉诺塔的层数:"))
hanoi(n,'X','Y','Z')