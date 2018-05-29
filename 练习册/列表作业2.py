product = [["Iphone",6888],["Mropro",14860],["xiaomi6",2499],["coffee",32],["Book",80],["Nike shoes",799]]
shopping_car = []
while True:
    print("------------商品列表----------")
    for index, i in enumerate(product):
        print('{0},{1},{2}'.format(index, i[0], i[1]))
    choice = input("亲，你想买什么？请输入商品编号：")
    if choice.isdigit():
        choice = int(choice)
        shopping_car.append(product[choice])
        print("Odded %s into shopping car"% product[choice ])
    elif choice == "q":
        print("您的购物车有如下商品")
        for index,each in enumerate (shopping_car):
            print(index,each[0],each[1])
        break

        有如下问题：如何保证购物车退出时的列表和商品列表的编号是一致的。
        可以继续优化。







