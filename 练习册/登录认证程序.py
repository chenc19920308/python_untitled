username_list = ["a","b","c","d"]
password_list = ["A","B","C","D"]
count = 0
while count < 3:
    user_name = input("请输入您的用户名：")
    pass_name = input("请输入您的用户名密码：")
    if user_name  in username_list and pass_name in password_list and username_list.index(user_name)==password_list.index(pass_name):
        print("欢迎 %s 用户"%user_name )
        break
    else:
        print("用户名或密码有误，请重新登录")
        count += 1
        if count == 3:
            print("您已经登录三次，请下次再登录")
            break

