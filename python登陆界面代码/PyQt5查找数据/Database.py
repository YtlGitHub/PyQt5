import sqlite3
import time


class Database:
    """为登录界面所提供数据库操作的类"""

    def __init__(self, db):
        self._database = db
        self.create_table()

    @property  # 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。需要注意的是，如果类中只包含该方法，那么 database 属性将是一个只读属性。也就是说，在使用 Database 类时，无法对 database 属性重新赋值，即运行代码会报错
    def database(self):
        return self._database

    @database.setter  # 而要想实现修改 database 属性的值，还需要为 database 属性添加 setter 方法，就需要用到 setter 装饰器
    def database(self, db):
        self._database = db

    def create_table(self):
        """创建一个数据库"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = "CREATE TABLE IF NOT EXISTS data(username TEXT, password TEXT, created_time TEXT)"
        cursor.execute(sql)
        if not self.is_has('admin'):  # 管理员的用户名一定为 admin ！
            created_time = self.get_time()
            default = "INSERT INTO data(username, password, created_time) VALUES('admin', 'admin123', ?)"  # 设置初始的账号密码
            cursor.execute(default, (created_time,))
        connect.commit()
        connect.close()

    def insert_table(self, username, password):
        """向数据库中插入元素"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        if self.is_has(username):
            # print("Already exits username {}".format(username))  # 测试使用
            return True  # 已经有该元素的时候返回一个 True 提供外界接口
        else:
            created_time = self.get_time()
            sql = 'INSERT INTO data (username, password, created_time) VALUES(?,?,?)'
            cursor.execute(sql, (username, password, created_time))
            connect.commit()
        connect.close()

    def read_table(self):
        """读取数据库中的所有元素"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT * FROM data ORDER BY username'
        result = cursor.execute(sql)
        data = result.fetchall()
        connect.commit()
        connect.close()
        return data

    def update_table(self, username, password):
        """更新数据库中的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'UPDATE data SET password =? WHERE username=? '
        cursor.execute(sql, (password, username))
        connect.commit()
        connect.close()

    def find_password_by_username(self, username):
        """根据用户名来查找用户的密码"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT password FROM data WHERE username=?'
        result = cursor.execute(sql, (username,))
        connect.commit()
        found_data = result.fetchall()
        connect.close()
        return found_data

    def delete_table_by_username(self, username):
        """通过用户名称删除数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'DELETE FROM data WHERE  username=?'
        cursor.execute(sql, (username,))
        connect.commit()
        connect.close()

    def is_has(self, username):
        """判断数据库中是否包含用户名信息"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT * FROM data WHERE username=?'
        result = cursor.execute(sql, (username,))
        connect.commit()
        all_data = result.fetchall()
        connect.close()
        if all_data:
            return True
        else:
            return False

    def clear(self):
        """清空所有的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = "DELETE FROM data"
        cursor.execute(sql)
        connect.commit()
        connect.close()

    @staticmethod  # 使用staticmethod的代码, 用staticmethod包装的方法可以内部调用, 也可以通过类访问或类实例化访问。两个代码的区别后者是加了@staticmethod, 把方法checkind()放入类中，既有在类内调用，也可以在类外通过类来调用（不一定要实例化）
    def get_time():
        date = time.localtime()
        created_time = "{}-{}-{}-{}:{}:{}".format(date.tm_year, date.tm_mon,
                                                  date.tm_mday,
                                                  date.tm_hour, date.tm_min,
                                                  date.tm_sec)
        return created_time


if __name__ == '__main__':
    data = Database('./data.db')
    # data.insert_table('ytl', '123456')
    data_ = data.read_table()
    print(data_)
    # for i in range(23):  # 简单的创建用户
    #     data.insert_table(chr(i + 65) * 5, chr(i + 65) + chr(i + 66) * 5)
