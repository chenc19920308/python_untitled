import configparser
conf = configparser.ConfigParser()

conf.read("gro.ini")
# print(dir(conf))    所有功能道出了
# print(conf.options("group1"))  导出group1的所有key
# print(conf["group1"]["k2"])   导出k2 的值

# 增加
# conf.add_section("group3")
# conf['group3']['name'] = "chenc"
# conf['group3']["age"] = "27"
#
# conf.write(open('new_gro.ini',"w"))
# 修改
# conf.set('group2','k1','22222')
# conf.write(open('gro2.ini','w'))


conf.remove_option('group1','k2')  #删除
conf.remove_section('group1')  #作用和上面一样
conf.write(open('gro3.ini',"w"))
