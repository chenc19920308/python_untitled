place_name = {
"安徽":{
                    "合肥":["东市","西市","中市","郊区","长丰","肥东","肥西"],
                    "芜湖":["鸠江","镜湖","新芜","马塘","芜湖","繁昌","南陵"],
                    "蚌埠":["东市","西市","中市","郊区","怀远","固镇","五河"],
                    "淮南":["谢家集","潘集","田家庵","大通","八公山","凤台"],
                    "安庆":["迎江","大观","郊区","桐城","宿松","怀宁","枞阳","潜山","太湖","望江","岳西"],
                    "阜阳":["颍上","颍州","颍东","颍泉","界首","涡阳","蒙城","太和","利辛","阜南","临泉"],
                    "铜陵":["铜官山","狮子山","郊区","铜陵县"],
                    "马鞍山":["金家庄","花山区","雨山区","向山区","当涂"],
                    "滁州":["琅琊","南谯","天长","明光","来安","全椒","定远","凤阳"],
                    "黄山":["屯溪","黄山","徽州","休宁","黟县","祁门县","歙县"],
                    "宿州":["埇桥","萧县","汤山","灵璧","泗县"],
                    "淮北":["杜集","相山","烈山","曲溪"],
                    "亳州":[],
                    "宣城":["宣州","宁国","郎溪","广德","绩溪","泾县","旌德"],
                    "六安":["金安","裕安","舒城","寿县","霍邱","霍山","金寨"],
                    "池州":["贵池","东至","石台","青阳"]
                    },
"香港":{
           "香港岛":["海上公园"],
           "九龙":["古惑仔","周星驰","奥特曼"],
           "新界":["黄赌毒"]},
"澳门":{
        "澳门半岛":["葡京"],
        "路环岛":["张柏芝"],
        "龙头湾":["迪士尼"]
}
}
while True:
    print("省份列表".center(26,"-"))
    prov_name = list(place_name.keys())
    for i in  prov_name :
        print (i)