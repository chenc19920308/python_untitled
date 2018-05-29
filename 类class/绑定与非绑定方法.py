#settings.py
HOST = '127.0.0.1'
PORT = 3306
DB_PATH = r'C:\Users\Administrator\PycharmProjects\test\面向对象编程\test1\db'

#test.py
import settings
class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    @classmethod
    def from_conf(cls):
        print(cls)
        return cls(settings.HOST,settings.PORT)

print(MySQL.from_conf) #<bound method MySQL.from_conf of <class '__main__.MySQL'>>
conn=MySQL.from_conf()

conn.from_conf() #对象也可以调用，但是默认传的第一个参数仍然是类