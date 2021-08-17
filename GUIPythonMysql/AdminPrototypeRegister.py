import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QAbstractItemView, QMessageBox, QTableWidgetItem, \
    QLineEdit, QPushButton, QHeaderView, QLabel, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from Database2 import Database2


class AdminPrototypeRegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)  # 添加表格对象
        # self.database = Database('./data2.db')
        self.database2 = Database2()
        self.check_list = []  # 保存所有的选择框
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("查找YTL的机型信息")
        self.setFixedSize(1600, 900)
        self.font = QFont("arial")
        self.setFont(self.font)
        self.setWindowIcon(QIcon("./IMG/wanywn.png"))  # 设置图标
        self.add_label()  # 添加界面上的标签控件
        self.add_table()  # 制定表格格式
        self.add_button()  # 添加按钮并绑定事件
        self.add_line_edit()  # 制定输入框位置
        self.get_all_prototype()  # 获取所有数据并展示

    def add_table(self):
        """添加数据表格"""
        self.table.setFixedWidth(1590)  # 设置宽度
        self.table.setFixedHeight(600)  # 设置高度
        self.table.move(10, 30)  # 设置显示的位置
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.table.horizontalHeader().setFont(self.font)  # 设置一下字体
        # self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # 只能单选
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.table.setColumnCount(13)  # 设置列数
        data_liat_field = self.database2.read_table_field()  # 调用Database2.read_table_field()自定义方法，读取表格的字段
        data_liat_field.insert(0, "Choice")  # 在列表下标为0的地方插入”Choice“字段
        self.table.setHorizontalHeaderLabels(data_liat_field)  # 设置首行字段
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格中的内容设置为无法修改
        self.table.verticalHeader().hide()  # 把序号隐藏
        self.table.setSortingEnabled(False)  # 自动排序

    def add_line_edit(self):
        move_x = 10
        move_y = 665
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

        self.where_edit = QLineEdit(self)
        self.where_edit.setFixedSize(fixe_x+300, fixe_y)
        self.where_edit.move(move_x, move_y + 80)
        self.where_edit.setPlaceholderText('where')

        self.insert_edit = QLineEdit(self)
        self.insert_edit.setFixedSize(fixe_x + 300, fixe_y)
        self.insert_edit.move(move_x, move_y + 120)
        self.insert_edit.setPlaceholderText('insert into table_name() values()')

        self.field_update_edit = QLineEdit(self)
        self.field_update_edit.setFixedSize(fixe_x, fixe_y)
        self.field_update_edit.move(move_x, move_y + 160)
        self.field_update_edit.setPlaceholderText('field_update')

        self.value_update_edit = QLineEdit(self)
        self.value_update_edit.setFixedSize(fixe_x, fixe_y)
        self.value_update_edit.move(move_x+110, move_y + 160)
        self.value_update_edit.setPlaceholderText('value_update')

        self.id_update_edit = QLineEdit(self)
        self.id_update_edit.setFixedSize(fixe_x, fixe_y)
        self.id_update_edit.move(move_x+220, move_y + 160)
        self.id_update_edit.setPlaceholderText('id_uodate')

        self.delete_edit = QLineEdit(self)
        self.delete_edit.setFixedSize(fixe_x, fixe_y)
        self.delete_edit.move(move_x, move_y + 200)
        self.delete_edit.setPlaceholderText('delete')

    def add_button(self):
        """添加界面上的按钮控件"""
        move_x = 10
        move_y = 630
        self.add_button_ = QPushButton(self)
        self.add_button_.setText("All")
        self.add_button_.setToolTip("展示所有数据")
        self.add_button_.move(move_x, move_y)
        self.add_button_.clicked.connect(self.get_all_prototype)

        self.add_button_ = QPushButton(self)
        self.add_button_.setText("QUERY")
        self.add_button_.setToolTip("查找数据")
        self.add_button_.move(move_x+115, move_y+35)
        self.add_button_.clicked.connect(self.get_select_prototype)

        self.add_button_ = QPushButton(self)
        self.add_button_.setText("WHERE")
        self.add_button_.setToolTip("自定义条件查询")
        self.add_button_.move(move_x + 415, move_y + 115)
        self.add_button_.clicked.connect(self.get_select_prototype_where)

        self.add_button_ = QPushButton(self)
        self.add_button_.setText("INSERT")
        self.add_button_.setToolTip("插入数据")
        self.add_button_.move(move_x + 415, move_y + 155)
        self.add_button_.clicked.connect(self.insert_prototype)

        self.add_button_ = QPushButton(self)
        self.add_button_.setText("UPDATE")
        self.add_button_.setToolTip("修改数据")
        self.add_button_.move(move_x + 335, move_y + 195)
        self.add_button_.clicked.connect(self.update_prototype)

        self.add_button_ = QPushButton(self)
        self.add_button_.setText("DELETE")
        self.add_button_.setToolTip("删除数据")
        self.add_button_.move(move_x+115, move_y + 235)
        self.add_button_.clicked.connect(self.delete_prototype)

    def add_label(self):
        """添加界面上的标签控件"""
        fixe_x = 200
        fixe_y = 30
        move_x = 10
        move_y = 0
        self.username_label = QLabel(self)
        self.username_label.setFixedSize(fixe_x, fixe_y)
        self.username_label.move(move_x, move_y)
        self.username_label.setText('欢迎进入YTLMySQL系统')

    def get_all_prototype(self):
        """获取所有的机型信息"""
        self.table.setRowCount(0)  # 将表格的行数重置为0
        data_all = self.database2.read_table()  # 调用Database2.read_table自定义方法，读取表格里面的所有数据
        self.add_row(data_all)

    def get_select_prototype(self):
        key = self.key_edit.text()  # 获取输入框文本
        value = self.value_edit.text()  # 获取输入框文本
        if all((key, value)):  # 判断是否有输入文本，有输入就往下走，没有输入就提示，输入框为空
            has_key = self.database2.is_has_key(key)  # 判断是否有这个字段，有就往下走，没有就提示，没有这个字段
            if has_key:
                has_value = self.database2.is_has_value(key, value)  # 判断是否有这个字段的值，有就往下走，没有就提示没有这个值
                if has_value:
                    self.table.setRowCount(0)  # 将表格的行数重置为0
                    data_select = self.database2.select_prototype_info(key, value)  # 查询元素
                    self.add_row(data_select)
                else:
                    QMessageBox.critical(self, 'Error', "没有这个机型")
            else:
                QMessageBox.critical(self, 'Error', "没有这个字段")
        else:
            QMessageBox.critical(self, 'Error', "key/values值为空")

    def get_select_prototype_where(self):
        where = self.where_edit.text()  # 获取输入的条件查询文本
        if where:
            data_where = self.database2.select_prototype_info_where(where)
            if data_where:
                self.table.setRowCount(0)  # 将表格的行数重置为0
                self.add_row(data_where)
            else:
                QMessageBox.critical(self, 'Error', "sql条件语法有误")
        else:
            QMessageBox.critical(self, 'Error', "where输入框为空")

    def insert_prototype(self):
        """插入数据"""
        inser_sql = self.insert_edit.text()  # 获取插入的数据
        if inser_sql:
            set_inser_data = self.database2.insert_prototype_info(inser_sql)  # 调用Databases2.insert_prototype_info()自定义MySQL语句生成提交到mysql库
            if set_inser_data:
                self.get_all_prototype()  # 获取所有信息并展示在GUI表上面
            else:
                QMessageBox.critical(self, 'Error', "sql语法输入有误")
        else:
            QMessageBox.critical(self, 'Error', "插入数据框为空")

    def update_prototype(self):
        """修改数据"""
        field_update_data = self.field_update_edit.text()  # 获取修改的数据
        value_update_data = self.value_update_edit.text()
        id_update_data = self.id_update_edit.text()
        if all((field_update_data, value_update_data, id_update_data)):
            update_data = self.database2.update_prototype_info(field_update_data, value_update_data, id_update_data)
            if update_data:
                self.get_all_prototype()  # 获取所有信息并展示在GUI表上面
        else:
            QMessageBox.critical(self, 'Error', 'field_update/value_update/value_update为空')

    def delete_prototype(self):
        delete_id = self.delete_edit.text()  # 获取删除输入框的id
        if delete_id:
            print(delete_id)
            delete_data = self.database2.delete_prototype_info(delete_id)
            if delete_data:
                self.get_all_prototype()
            else:
                QMessageBox.critical(self, 'Error', '没有这个数据id')
        else:
            QMessageBox.critical(self, 'Error', '输入id框为空')

    def add_row(self,data):
        """在表格上添加一行新的内容"""
        for i in data:
            row = self.table.rowCount()  # 表格的行数
            self.table.setRowCount(row + 1)  # 添加一行表格
            # 设置复选框
            widget = QWidget()
            check = QCheckBox()
            self.check_list.append(check)  # 添加到复选框列表中
            check_lay = QHBoxLayout()
            check_lay.addWidget(check)
            check_lay.setAlignment(Qt.AlignCenter)
            widget.setLayout(check_lay)
            self.table.setCellWidget(row, 0, widget)
            for j in range(len(i)):
                self.table.setItem(row, j+1, QTableWidgetItem(str(i[j])))  # 将用户信息插入到表格中

# =================================================================

    def set_main_window(self, widget):
        self.main_window = widget

    def delete_row(self, i):
        row = self.table.rowCount()  # 表格的行数
        self.table.removeRow(i)  # removeRow(去除这一行)

    def all_prototype_info(self):
        """重新加载数据库并显示"""
        self.table.clearContents()  # 清空表格的内容
        self.check_list.clear()  # 检查列表清除
        self.table.setRowCount(0)  # 将表格的行数重置为0
        self.database2.create_table()
        self.get_all_prototype()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prototype_register_window = AdminPrototypeRegisterWindow()
    prototype_register_window.show()
    sys.exit(app.exec_())