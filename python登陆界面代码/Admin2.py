import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QAbstractItemView, QMessageBox, QTableWidgetItem, \
    QLineEdit, QPushButton, QHeaderView, QLabel, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from Database import Database


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)  # 添加表格对象
        self.database = Database('./data.db')
        self.check_list = []  # 保存所有的选择框
        self.show_password_flag = False  # 是否显示原密码
        self.select_all_flag = False  # 是否选择全部
        self.main_window = None
        self.set_ui()

    def set_main_window(self, widget):
        self.main_window = widget

    def set_ui(self):
        self.setWindowTitle("Management page")
        self.setFixedSize(1200, 900)
        self.font = QFont("Consolas")
        self.setFont(self.font)
        self.setWindowIcon(QIcon("./IMG/python-logo.png"))  # 设置图标
        self.add_table()  # 制定表格格式
        self.get_all_user()  # 展示数据
        self.add_line_edit()  # 制定输入框位置
        self.add_button()  # 添加按钮并绑定事件

    def add_table(self):
        """添加数据表格"""
        self.table.setFixedWidth(1020)  # 设置宽度
        self.table.setFixedHeight(600)  # 设置高度
        self.table.move(10, 30)  # 设置显示的位置
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.table.horizontalHeader().setFont(self.font)  # 设置一下字体
        # self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # 只能单选
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.table.setColumnCount(5)  # 设置列数
        self.table.setHorizontalHeaderLabels(["Choice", "username", "password", 'created_time', 'user5'])  # 设置首行
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格中的内容设置为无法修改
        self.table.verticalHeader().hide()  # 把序号隐藏
        self.table.setSortingEnabled(False)  # 自动排序

    def get_all_user(self):
        """获取所有的用户信息"""
        data = self.database.read_table()  # 从数据库中获取用户信息，用户信息以 username, password, created_time 形式返回
        print(data)
        for user in data:
            print(user)
            self.add_row(user[0], user[1], user[2])

    def add_row(self, username, password, created_time):
        """在表格上添加一行新的内容"""
        row = self.table.rowCount()  # 表格的行数
        print(row)
        self.table.setRowCount(row + 1)  # 添加一行表格
        self.table.setItem(row, 1, QTableWidgetItem(str(username)))  # 将用户信息插入到表格中
        self.table.setItem(row, 2, QTableWidgetItem(str(password)))
        self.table.setItem(row, 3, QTableWidgetItem(str(created_time)))
        self.table.setItem(row, 4, QTableWidgetItem(str('user5')))
        # 设置复选框
        widget = QWidget()
        check = QCheckBox()
        self.check_list.append(check)  # 添加到复选框列表中
        check_lay = QHBoxLayout()
        check_lay.addWidget(check)
        check_lay.setAlignment(Qt.AlignCenter)
        widget.setLayout(check_lay)
        self.table.setCellWidget(row, 0, widget)

    def add_button(self):
        """添加界面上的按钮控件"""
        self.add_button_ = QPushButton(self)
        self.add_button_.setText("Add")
        self.add_button_.setToolTip("Add a new user with the username and password in the input box")
        self.add_button_.move(1020, 700)
        self.add_button_.clicked.connect(self.add_user)

    def add_line_edit(self):
        self.username_edit = QLineEdit(self)
        self.username_edit.setFixedSize(240, 40)
        self.username_edit.move(760, 700)
        self.username_edit.setPlaceholderText('username')

        self.password_edit = QLineEdit(self)
        self.password_edit.setFixedSize(240, 40)
        self.password_edit.move(760, 760)
        self.password_edit.setPlaceholderText('password')
        self.password_edit.setEchoMode(QLineEdit.Password)

    def add_user(self):
        """一行一行的添加数据"""
        username = self.username_edit.text()
        password = self.password_edit.text()
        if all((username, password)):
            flag = self.database.insert_table(username, password)
            if flag:
                QMessageBox.critical(self, 'Error', 'Already exists the username {}, please use another username'.format(username))
            else:
                self.add_row(username, password, self.database.get_time())
            self.username_edit.setText('')  # 清空输入的用户信息
            self.password_edit.setText('')
        else:
            QMessageBox.critical(self, 'Error', "Please fill in the blanks")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_window = AdminWindow()
    admin_window.show()
    sys.exit(app.exec_())