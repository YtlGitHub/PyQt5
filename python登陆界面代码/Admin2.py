import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QAbstractItemView, QMessageBox, QTableWidgetItem, \
    QLineEdit, QPushButton, QHeaderView, QLabel, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from Database2 import Database2


class Admin2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)  # 添加表格对象
        # self.database = Database('./data2.db')
        self.database2 = Database2()
        self.check_list = []  # 保存所有的选择框
        self.show_password_flag = False  # 是否显示原密码
        self.select_all_flag = False  # 是否选择全部
        self.main_window = None
        self.set_ui()

    def set_main_window(self, widget):
        self.main_window = widget

    def set_ui(self):
        self.setWindowTitle("Ytl的机型信息")
        self.setFixedSize(1600, 900)
        self.font = QFont("Consolas")
        self.setFont(self.font)
        self.setWindowIcon(QIcon("./IMG/wanywn.png"))  # 设置图标
        self.add_table()  # 制定表格格式
        self.add_button()  # 添加按钮并绑定事件
        self.add_line_edit()  # 制定输入框位置

    def add_table(self):
        """添加数据表格"""
        self.table.setFixedWidth(1590)  # 设置宽度
        self.table.setFixedHeight(600)  # 设置高度
        self.table.move(10, 10)  # 设置显示的位置
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.table.horizontalHeader().setFont(self.font)  # 设置一下字体
        # self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # 只能单选
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.table.setColumnCount(13)  # 设置列数
        self.table.setHorizontalHeaderLabels(["Choice", "id", "id_name", "de", "brand", "pv", "OS", "m_name", "IMEI", "name", "user_name", "borrow_time", "still_time"])  # 设置首行
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格中的内容设置为无法修改
        self.table.verticalHeader().hide()  # 把序号隐藏
        self.table.setSortingEnabled(False)  # 自动排序

    def get_all_prototype(self):
        """获取所有的机型信息"""
        self.table.setRowCount(0)  # 将表格的行数重置为0
        data = self.database2.read_table()  # 从数据库中获取用户信息，用户信息以 username, password, created_time 形式返回
        for user in data:
            self.add_row(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11])

    def get_select_prototype(self):
        self.table.setRowCount(0)  # 将表格的行数重置为0
        key = self.key_edit.text()  # 获取输入框文本
        value = self.value_edit.text()  # 获取输入框文本
        if all((key, value)):  # 判断是否有输入文本，有输入就往下走，没有输入就提示，输入框为空
            has_key = self.database2.is_has_key(key)  # 判断是否有这个字段，有就往下走，没有就提示，没有这个字段
            if has_key:
                has_value = self.database2.is_has_value(key, value)  # 判断是否有这个字段的值，有就往下走，没有就提示没有这个值
                if has_value:
                    data = self.database2.select_prototype_info(key, value)  # 查询元素
                    for user in data:
                        self.add_row(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11])
                else:
                    QMessageBox.critical(self, 'Error', "没有这个机型")
            else:
                QMessageBox.critical(self, 'Error', "没有这个字段")
        else:
            QMessageBox.critical(self, 'Error', "key/values值为空")

    def add_row(self, id, id_name, de, brand, pv, OS, m_name, IMEI, name, user_name, borrow_time, still_time):
        """在表格上添加一行新的内容"""
        row = self.table.rowCount()  # 表格的行数
        self.table.setRowCount(row + 1)  # 添加一行表格
        self.table.setItem(row, 1, QTableWidgetItem(str(id)))  # 将用户信息插入到表格中
        self.table.setItem(row, 2, QTableWidgetItem(str(id_name)))
        self.table.setItem(row, 3, QTableWidgetItem(str(de)))
        self.table.setItem(row, 4, QTableWidgetItem(str(brand)))
        self.table.setItem(row, 5, QTableWidgetItem(str(pv)))
        self.table.setItem(row, 6, QTableWidgetItem(str(OS)))
        self.table.setItem(row, 7, QTableWidgetItem(str(m_name)))
        self.table.setItem(row, 8, QTableWidgetItem(str(IMEI)))
        self.table.setItem(row, 9, QTableWidgetItem(str(name)))
        self.table.setItem(row, 10, QTableWidgetItem(str(user_name)))
        self.table.setItem(row, 11, QTableWidgetItem(str(borrow_time)))
        self.table.setItem(row, 12, QTableWidgetItem(str(still_time)))
        # 设置复选框
        widget = QWidget()
        check = QCheckBox()
        self.check_list.append(check)  # 添加到复选框列表中
        check_lay = QHBoxLayout()
        check_lay.addWidget(check)
        check_lay.setAlignment(Qt.AlignCenter)
        widget.setLayout(check_lay)
        self.table.setCellWidget(row, 0, widget)

    def delete_row(self, i):
        row = self.table.rowCount()  # 表格的行数
        self.table.removeRow(i)  # removeRow(去除这一行)

    def add_button(self):
        """添加界面上的按钮控件"""
        move_x = 10
        move_y = 620
        self.add_button_ = QPushButton(self)
        self.add_button_.setText("All")
        self.add_button_.setToolTip("展示所有数据")
        self.add_button_.move(move_x, move_y)
        self.add_button_.clicked.connect(self.get_all_prototype)

        self.add_button_ = QPushButton(self)
        self.add_button_.setText("select")
        self.add_button_.setToolTip("查找数据")
        self.add_button_.move(move_x+115, move_y+35)
        self.add_button_.clicked.connect(self.get_select_prototype)

        # self.main_window_button.setFixedSize(200, 40)

    def show_main_window(self):
        self.main_window.show()

    def add_line_edit(self):
        move_x = 10
        move_y = 655
        fixe_x = 100
        fixe_y = 30
        self.key_edit = QLineEdit(self)
        self.key_edit.setFixedSize(fixe_x, fixe_y)
        self.key_edit.move(move_x, move_y)
        self.key_edit.setPlaceholderText('key')

        self.value_edit = QLineEdit(self)
        self.value_edit.setFixedSize(fixe_x, fixe_y)
        self.value_edit.move(move_x, move_y+40)
        self.value_edit.setPlaceholderText('value')
        # self.value_edit.setEchoMode(QLineEdit.Password)

    # def add_user(self):
    #     """一行一行的添加数据"""
    #     username = self.username_edit.text()
    #     password = self.password_edit.text()
    #     if all((username, password)):
    #         flag = self.database.insert_table(username, password)
    #         if flag:
    #             QMessageBox.critical(self, 'Error', 'Already exists the username {}, please use another username'.format(username))
    #         else:
    #             self.add_row(username, password, self.database.get_time())
    #         self.username_edit.setText('')  # 清空输入的用户信息
    #         self.password_edit.setText('')
    #     else:
    #         QMessageBox.critical(self, 'Error', "Please fill in the blanks")

    def all_prototype_info(self):
        """重新加载数据库并显示"""
        self.table.clearContents()  # 清空表格的内容
        self.check_list.clear()
        self.table.setRowCount(0)  # 将表格的行数重置为0
        self.database2.create_table()
        self.get_all_prototype()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_window = Admin2Window()
    admin_window.show()
    sys.exit(app.exec_())