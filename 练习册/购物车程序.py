product = [
    ["旅行箱",588],
    ["男士钱包",99],
    ["小罐茶叶",588],
    ["无线鼠标",45],
    ["32G优盘",20],
    ["江中牌健胃消食片",54],
    ["中性水笔",5],
    ["小米手环",256],
    ["iwatch",2500],
    ["波司登羽绒服",1200],
    ["iMacPro",5700]
]
u_budget = int(input("请输入本次购物预算："))
u_balance = u_budget
shopping_car = []
while True:
    print("本店商品列表如下".center(30,"-"))
    for index, p in enumerate(product):
        print(index, p[0], p[1])
    choice = input("请选择相应的商品编号进行购买：")
    if choice.isdigit():
        choice = int(choice)
        if  choice >= 0 and choice < len(product):
            if product[choice][1] <= u_balance :
                shopping_car.append(product[choice])
                u_balance  -= product[choice][1]
            else:
                print("余额不足，请充值。")
                break
        else:
            if choice >= len(product):
                print("本店无此商品")
                break
    else:
        if  choice == "q":
            print("您购买了如下商品：")
            for index,p in enumerate(shopping_car):
                print(index,p[0],p[1])
            print("一共消费额度：",u_budget - u_balance )
            print("剩余预算为：",u_balance )
        break