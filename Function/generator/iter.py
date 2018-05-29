class IT:
    def __init__(self):
        self.l = [1, 2, 3, 4, 5]
        self.i = iter(self.l)
    def __call__(self):  # 定义了__call__方法的类的实例是可调用的
        item = next(self.i)
        print("__call__ is called,which would return", item)
        return item
    def __iter__(self):  # 支持迭代协议(即定义有__iter__()函数)
        print("__iter__ is called!!")
        return iter(self.l)
it = IT()
for i in it:
    print(i)

it1 = iter(it,3)
print(it1)
for k in it1:
    print(k)