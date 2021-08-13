import sqlite3
import time
import pymysql


class Database2:
    """为登录界面所提供数据库操作的类"""
    def __init__(self, db_host="10.127.56.173", db_user="ytluser", db_pass="ytl", db_name="prototype_register"):
        self.connect = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name,charset='utf8')  # 打开数据库连接
        self.cursor = self.connect.cursor()  # 获取操作游标
        # self.create_table()

    @property  # 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。需要注意的是，如果类中只包含该方法，那么 database 属性将是一个只读属性。也就是说，在使用 Database 类时，无法对 database 属性重新赋值，即运行代码会报错
    def database(self):
        return self._database

    @database.setter  # 而要想实现修改 database 属性的值，还需要为 database 属性添加 setter 方法，就需要用到 setter 装饰器
    def database(self, db):
        self._database = db

    def read_table(self):
        """读取数据库中的所有元素"""
        sql = 'SELECT * FROM prototype_info'
        self.cursor.execute(sql)
        data2 = self.cursor.fetchall()
        self.connect.commit()
        self.connect.close()
        return data2

    def is_has(self, value):
        """判断数据库中是否包含id_name信息"""
        sql = 'SELECT * FROM prototype_info WHERE id_name=?'
        self.cursor.execute(sql, (value,))
        all_data = self.cursor.fetchall()
        self.connect.commit()
        self.connect.close()
        if all_data:
            return True
        else:
            return False

    def select_prototype_info(self, key, value):
        """指定条件查找数据"""
        sql = f'SELECT * FROM prototype_info WHERE {key}={value}'
        self.cursor.execute(sql)
        data_id_name = self.cursor.fetchall()
        self.connect.commit()
        self.connect.close()
        return data_id_name


if __name__ == '__main__':
    data = Database2()
    data_ = data.select_prototype_info("id_name", 20391)
    print(data_)
