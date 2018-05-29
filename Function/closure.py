def funcX():
    x = 9
    print('x')
    def funcY(y):
        return int(y)*x
    return funcY

i = funcX()
print(i(5))   # note: 内部函数对外部函数进行引用，此为闭包，只是引用，不能修改哟！
