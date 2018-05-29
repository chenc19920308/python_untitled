def collect(*params,**kwargs):
    print(params)
    print(kwargs)
    # print("There are %s parameters in all,"%len(params))
    # print("The second param is %s"%params[0])
#
#
a = [1,2,3,4,4]
b = {'a':3,'b':4}
collect(*a,**b)

# def foo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# foo(1,2,3,4,y=1,a=2,b=3,c=4)        Normal work






# a = collect(1,3,5,7,9)
# collect(2,7,3,a=9,b=89)
# print(a)
# print(collect(c=6,a=9,b=89))



# Unpack
# b = (123,345,6512,89)
# b = [123,345,6512,89]
# d = {1:2,2:3,3:4}
# print(collect(*d))
# word = "family"
# print(collect(*b))
# print(collect(*word))

#print(collect('faliy'))   meaning one params





# def collect(**kwargs):
#     print("There are %s parameters in all,"%len(kwargs))
#     print("There are:",kwargs)

# collect(c=6,a=9,b=89)

# a = {"djbc":2, "fhu":3, "d":4, "ef":5}     note:   keywords must be strings
# collect(**a)