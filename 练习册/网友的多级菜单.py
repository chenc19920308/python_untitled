zone = {
     '山东' : {
         '青岛' : ['四方','黄岛','崂山','李沧','城阳'],
         '济南' : ['历城','槐荫','高新','长青','章丘'],
         '烟台' : ['龙口','莱山','牟平','蓬莱','招远']
               },
     '江苏' : {
         '苏州' : ['沧浪','相城','平江','吴中','昆山'],
         '南京' : ['白下','秦淮','浦口','栖霞','江宁'],
         '无锡' : ['崇安','南长','北塘','锡山','江阴']
            },
     '浙江' : {
         '杭州' : ['西湖','江干','下城','上城','滨江'],
         '宁波' : ['海曙','江东','江北','镇海','余姚'],
         '温州' : ['鹿城','龙湾','乐清','瑞安','永嘉']
     },
     '安徽' : {
         '合肥' : ['蜀山','庐阳','包河','经开','新站'],
         '芜湖' : ['镜湖','鸠江','无为','三山','南陵'],
         '蚌埠' : ['蚌山','龙子湖','淮上','怀远','固镇']
     },
     '广东' : {
         '深圳' : ['罗湖','福田','南山','宝安','布吉'],
         '广州' : ['天河','珠海','越秀','白云','黄埔'],
         '东莞' : ['莞城','长安','虎门','万江','大朗']
     }
 }
province_list = list(zone.keys())
while True:
    print(" 省 ".center(50,'*'))
    for i in province_list:
        print(province_list.index(i)+1,i)
        pro_id = input("请输入省编号,或输入q(quit)退出：")
        if pro_id.isdigit():
            pro_id = int(pro_id)
            if pro_id > 0 and pro_id <= len(province_list):
                pro_name = province_list[pro_id-1]
                city_list = list(zone[pro_name].keys())
                while True:
                    print(" 市 ".center(50,'*'))
                    for v in city_list:
                        print(city_list.index(v)+1,v)
                        city_id = input("请输入市编号,或输入b(back)返回上级菜单，或输入q(quit)退出：")
                        if city_id.isdigit():
                            city_id = int(city_id)
                            if city_id > 0 and city_id <= len(city_list):
                                city_name = city_list[city_id-1]
                                town_list = zone[pro_name][city_name]
                                while True:
                                    print(" 县 ".center(50,'*'))
                                    for j in town_list:
                                        print(town_list.index(j)+1,j)
                                        back_or_quit = input("输入b(back)返回上级菜单，或输入q(quit)退出：")
                                        if back_or_quit == 'b':
                                            break
                                        elif back_or_quit == 'q':
                                            exit()
                                        else:
                                            print("输入非法！")
                            else:
                                print("编号%d不存在。"%city_id)
                        elif city_id == 'b':
                            break
                        elif city_id == 'q':
                            exit()
                        else:
                            print("输入非法!")
            else:
                print("编号%d不存在。"%pro_id)
        elif pro_id == "q":
            break
        else:
            print("输入非法!")