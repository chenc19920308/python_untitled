# 此模块用于生成和修改常见配置文档，当前模块的名称在 python 3.x 版本中变更为 configparser。
# ConfigParser模块在python3中修改为configparser.这个模块定义了一个ConfigParser类，
# 该类的作用是使用配置文件生效，配置文件的格式和windows的INI文件的格式相同
# 该模块的作用就是使用模块中的 RawConfigParser()、ConfigParser()、 SafeConfigParser()这三个方法（三者择其一）
# 创建一个对象使用对象的方法对指定的配置文件做增删改查操作。
import configparser
conf = configparser.ConfigParser()
conf.read("conf.ini")
# print(conf.sections())   #将bitbulcket.org和topsecret.server.com打印出来了。相当于key
# print(conf.default_section)#将"DEFAULT"打印出来了
# print(list(conf["bitbucket.org"].keys()))
# print(conf["bitbucket.org"]["User"])  #查到哦了
# for k in conf["bitbucket.org"]:
#     print(k)
# for k,v in conf["bitbucket.org"].items():
#     print(k,v)   #将DEFAULT和bitbucket.org中的key和value都打印出来了。
#     [DEFAULT]本身就是默认值，在每一个节点都会出现

#作参数的判断
if "user" in conf["bitbucket.org"]:
    print("in")


#修改

