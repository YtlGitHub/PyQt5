import sqlite3
import time
import pymysql


class Database2:
    """为登录界面所提供数据库操作的类"""
    db_host_gs = "10.127.56.173"
    db_host_jia = "192.168.43.136"
    db_host = db_host_jia

    def __init__(self, db_host="10.127.56.173", db_user="ytluser", db_pass="ytl", db_name="prototype_register"):
        print(db_host)
        self.connect = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')  # 打开数据库连接
        self.cursor = self.connect.cursor()  # 获取操作游标
        # print('连接成功')
        self.create_table()
        # self.insert_prototype_info()
        # self.connect.close()

    @property  # 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。需要注意的是，如果类中只包含该方法，那么 database 属性将是一个只读属性。也就是说，在使用 Database 类时，无法对 database 属性重新赋值，即运行代码会报错
    def database(self):
        return self._database

    @database.setter  # 而要想实现修改 database 属性的值，还需要为 database 属性添加 setter 方法，就需要用到 setter 装饰器
    def database(self, db):
        self._database = db

    def create_table(self):  # 创建表
        sql = "create table if not exists prototype_info(id int, id_name int, de varchar(255), brand varchar(255), pv int, OS varchar(255), m_name varchar(255), IMEI int, name varchar(255), user_name varchar(255), borrow_time date, still_time date)"
        self.cursor.execute(sql)
        self.connect.commit()
        #self.connect.close()

    def insert_prototype_info(self, sql):  # 插入数据,sql语句自己写
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            return True
        except:
            return False

    def read_table_field(self):  # 读取表里面元素的字段
        """读取表格字段"""
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = 'prototype_info';"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        data_list_field = []
        for i in range(len(data)):
            data_list_field.append(data[i][0])
        return data_list_field

    def read_table(self):
        """读取数据库中的所有元素"""
        sql = 'SELECT * FROM prototype_info'
        self.cursor.execute(sql)
        data_all = self.cursor.fetchall()
        self.connect.commit()
        return data_all

    def is_has_key(self, key):
        """判断数据库中是否包含key信息"""
        data_list_field = self.read_table_field()
        if key in data_list_field:
            return True
        else:
            return False

    def is_has_value(self, key, value):
        """查找是否有这个值"""
        sql = f'SELECT * FROM prototype_info WHERE {key}="{value}"'
        self.cursor.execute(sql)
        all_data = self.cursor.fetchall()
        self.connect.commit()
        if all_data:
            return True
        else:
            return False

    def select_prototype_info(self, key, value):
        """指定条件查找数据"""
        sql = f'SELECT * FROM prototype_info WHERE {key}="{value}"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.connect.commit()
        return data

    def select_prototype_info_where(self, where):
        """指定条件查找数据"""
        sql = f'SELECT * FROM prototype_info WHERE {where}'
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.connect.commit()
            return data
        except:
            return False

    def update_prototype_info(self, field, value, id_):
        """修改数据"""
        try:
            sql = f'update prototype_info set {field}="{value}" where id = {id_}'
            self.cursor.execute(sql)
            self.connect.commit()
            return True
        except:
            return False

    def delete_prototype_info(self, id_):
        """修改数据"""
        try:
            sql = f'delete from prototype_info where id = {id_}'
            self.cursor.execute(sql)
            self.connect.commit()
            return True
        except:
            return False


if __name__ == '__main__':
    data = Database2()
    # data_field = data.read_table_field()  # 获取字段
    #print(data_field)
    data.update_prototype_info('user_name','杨天龙',1)
    data_ = data.read_table()  # 读取所有数据
    print(data_)
