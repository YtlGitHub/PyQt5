import sqlite3
import time  # 导入时间
import pymysql  # 导入pymysql用来连接数据库
import yaml  # 导入yaml用来读取配置文件


class Database2:
    """为登录界面所提供数据库操作的类"""
    def __init__(self):
        db_data = self.read_yml()
        db_host = db_data["db_host"]
        # print("本地ip：", db_host)
        db_user = db_data["db_user"]
        # print("用户名：", db_user)
        db_pass = db_data["db_pass"]
        # print("用户密码：", db_pass)
        db_name = db_data["db_name"]
        # print("数据库名：", db_name)
        self.connect = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name, charset='utf8')  # 打开数据库连接
        # self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)  # 获取操作游标，加个pymysql.cursors.DictCursor是以字典类型返回结果
        self.cursor = self.connect.cursor()  # 获取操作游标以元祖类型返回结果
        # print('连接成功')
        self.create_table()  # 判断有无表，有就不创建，无就创建
        # self.cursor.close()  # 关闭操作游标
        # self.connect.close()  # 关闭数据库连接

    @property  # 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。需要注意的是，如果类中只包含该方法，那么 database 属性将是一个只读属性。也就是说，在使用 Database 类时，无法对 database 属性重新赋值，即运行代码会报错
    def database(self):
        return self._database

    @database.setter  # 而要想实现修改 database 属性的值，还需要为 database 属性添加 setter 方法，就需要用到 setter 装饰器
    def database(self, db):
        self._database = db

    def read_yml(self):
        with open("db_data.yml", "r", encoding="utf-8") as f:
            # Loader=yaml.FullLoader 这个表示如果您是触发警告的 Python 代码的作者/维护者，停止收到警告的最佳方法是指定Loader=参数
            # BaseLoader
            # 只加载最基本的 YAML。所有标量都作为字符串加载。
            # SafeLoader
            # 安全地加载 YAML 语言的子集。建议加载不受信任的输入。
            # FullLoader
            # 加载完整的 YAML 语言。避免任意代码执行。这是当前（PyYAML 5.1+）调用的默认加载器yaml.load(input)（发出警告后）。
            db_data = yaml.load(f.read(), Loader=yaml.FullLoader)  # 用字典的方式读取db_data.yml数据db_data={'db_host': 'localhost', # 'db_user': 'ytluser', 'db_pass': 'ytl', 'db_name': 'db01', 'db_table': 'prototype_info'}
            return db_data

    def write_yml(self):
        db_data = self.read_yml()
        with open("db_data1.yml", "w", encoding="utf-8") as f:
            yaml.dump(db_data, stream=f, allow_unicode=True)

    def create_table(self):  # 创建表
        sql = "CREATE TABLE IF NOT EXISTS AdminData(username varchar(25) not null, password varchar(25) not null, created_time date)character set utf8 collate utf8_general_ci"
        self.cursor.execute(sql)
        sql = "CREATE TABLE IF NOT EXISTS prototype_info(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, id_name INT not null, de VARCHAR(100), brand VARCHAR(100), pv int, os varchar(255), m_name varchar(255), IMEI bigint(15), name varchar(255), user_name varchar(255), borrow_time date, still_time date)character set utf8 collate utf8_general_ci"
        self.cursor.execute(sql)
        if not self.is_has_admin('admin'):  #
            created_time = self.get_time()  # 设置当前添加的时间
            default = f"insert into AdminData(username, password, created_time) values('admin', 'admin123', '{created_time}')"
            self.cursor.execute(default)
        if not self.is_has_admin('ytl123'):  #
            created_time = self.get_time()  # 设置当前添加的时间
            default2 = f"insert into AdminData(username, password, created_time) values('ytl123', '123456', '{created_time}')"
            self.cursor.execute(default2)
        if not self.is_has_value('id', '1'):  #
            borrow_time = self.get_time()  # 设置当前添加的时间
            default3 = f"insert into prototype_info(id, id_name, de, brand, pv, os, m_name, IMEI, name, user_name, borrow_time, still_time) values(1, 19066, 'de', 'brand', 11, 'V11.1', 'm_name', IMEI, 'name', 'user_name', '{borrow_time}', null)"
            self.cursor.execute(default3)
        self.connect.commit()
        #self.connect.close()

    def clear(self):  # 删除表里面的所有数据
        sql = "DELETE FROM AdminData"
        self.cursor.execute(sql)
        self.connect.commit()

    def update_table(self, username, password):
        sql = f"UPDATE AdminData SET password='{password}' WHERE username='{username}'"
        self.cursor.execute(sql)
        self.connect.commit()

    def insert_prototype_info(self, sql):  # 插入数据,sql语句自己写
        try:
            print(sql)
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

    def read_table(self, table_name='prototype_info'):
        """读取数据库中的所有元素"""
        sql = f'SELECT * FROM {table_name}'
        self.cursor.execute(sql)
        data_all = self.cursor.fetchall()
        self.connect.commit()
        return data_all

    def is_has_key(self, field):
        """判断数据库中是否包含field字段信息"""
        data_list_field = self.read_table_field()
        if field in data_list_field:
            return True
        else:
            return False

    def is_has_admin(self, username):
        """查找是否有这个用户"""
        sql = f'SELECT * FROM AdminData WHERE username="{username}"'
        self.cursor.execute(sql)
        all_data = self.cursor.fetchall()
        return all_data

    def insert_table(self, username, password):  # 添加管理员用户账户和密码
        if self.is_has_admin(username):  # 先判断是否已有该用户
            return True  # 如已经有该用户的时候返回一个 True 提供外界接口
        else:  # 如没有就添加用户
            created_time = self.get_time()  # 设置当前添加的时间
            sql = f"insert into AdminData(username, password, created_time) values('{username}', '{password}', '{created_time}')"
            self.cursor.execute(sql)
            self.connect.commit()

    def delete_table_by_username(self, username):  # 根据用户名来删除用户
        sql = f"delete from AdminData where username='{username}'"
        self.cursor.execute(sql)
        self.connect.commit()

    def is_has_value(self, key, value):
        """查找是否有这个值"""
        sql = f'SELECT * FROM prototype_info WHERE {key}="{value}"'
        try:
            self.cursor.execute(sql)
            all_data = self.cursor.fetchall()
            return all_data
        except:
            return False

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

    @staticmethod  # 使用staticmethod的代码, 用staticmethod包装的方法可以内部调用, 也可以通过类访问或类实例化访问。两个代码的区别后者是加了@staticmethod, 把方法checkind()放入类中，既有在类内调用，也可以在类外通过类来调用（不一定要实例化）
    def get_time():
        date = time.localtime()
        created_time = "{}-{}-{}-{}:{}:{}".format(date.tm_year, date.tm_mon, date.tm_mday, date.tm_hour, date.tm_min, date.tm_sec)
        return created_time


if __name__ == '__main__':
    data = Database2()
    data.create_table()
    data_ = data.read_table()  # 读取所有数据
    for i in data_:
        print(i)
    #print(data_)
