# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 350, 350)  # 确定窗口位置大小
        self.setWindowTitle('点击按钮关闭窗口')  # 设置窗口标题
        quit = QPushButton('Close', self)  # button 对象
        quit.setGeometry(10, 10, 60, 35)  # 设置按钮的位置 和 大小
        quit.setStyleSheet("background-color: red")  # 设置按钮的风格和颜色
        quit.clicked.connect(self.close)  # 点击按钮之后关闭窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()  # 实体化 类
    win.show()
    sys.exit(app.exec_())