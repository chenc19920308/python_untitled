import math
class Circle:
    def __init__(self,radius): #圆的半径radius
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2 #计算面积

    @property
    def perimeter(self):
        return 2*math.pi*self.radius #计算周长

c=Circle(10)
print(c.radius)
print(c.area) #可以向访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值
print(c.perimeter) #同上


# class Foo:
#     def __init__(self,val):
#         self.__NAME=val        #将所有的数据属性都隐藏起来
#
#     @property
#     def name(self):
#         return self.__NAME    #obj.name访问的是self.__NAME(这也是真实值的存放位置)
#
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):     #在设定值之前进行类型检查
#             raise TypeError('%s must be str' %value)
#         self.__NAME=value          #通过类型检查后,将值value存放到真实的位置self.__NAME
#
#     @name.deleter
#     def name(self):
#         raise TypeError('Can not delete')
#
# f=Foo('egon')
# print(f.name)
# f.name=10     #抛出异常'TypeError: 10 must be str'
# del f.name     #抛出异常'TypeError: Can not delete'