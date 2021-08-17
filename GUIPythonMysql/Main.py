import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from YtlBlog import YtlBlog
from GuessNumber import GuessNumber
import random


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main page')
        self.setWindowIcon(QIcon('./IMG/logo.png'))
        self.setFixedSize(1200, 700)
        self.setFont(QFont('arial'))
        a = random.randint(0, 6)
        self.setStyleSheet(f"background-image: url('./IMG/{a}.jpg'); background-repeat: no repeat")
        # self.setWindowOpacity(0.9)
        self.YtlBlog_win = YtlBlog()
        self.guess_number_win = GuessNumber()
        self.set_ui()

    def set_ui(self):
        self.number()

    def number(self):
        number_font = QFont()
        number_font.setFamily('arial')
        number_font.setPixelSize(30)
        fixe_x = 100
        fixe_y = 100
        move_x = 50
        move_y = 50
        a_x = 100
        a_y = 0

        self.YtlBlog_button = QPushButton(self)  # 创建一个YtlBlog花按钮
        self.YtlBlog_button.setFixedSize(fixe_x + 20, fixe_y)  # 设置YtlBlog按钮大小
        self.YtlBlog_button.setFont(number_font)  # 设置YtlBlog按钮字体
        self.YtlBlog_button.move(move_x, move_y)  # 设置YtlBlog按钮位置
        self.YtlBlog_button.setText('YtlBlog')

        self.determine_button = QPushButton(self)  # 创建一个猜数字按钮
        self.determine_button.setFixedSize(fixe_x, fixe_y)  # 设置猜数字按钮大小
        self.determine_button.setFont(number_font)  # 设置猜数字按钮字体
        self.determine_button.move(move_x + 2*a_x, move_y + a_y)  # 设置猜数字按钮位置
        self.determine_button.setText('猜数字')

        self.YtlBlog_button.clicked.connect(self.ytl_blog)  # 打开YtlBlog博客
        self.determine_button.clicked.connect(self.guess_number)  # 猜数字

    def ytl_blog(self):
        self.YtlBlog_win.show()

    def guess_number(self):
        self.guess_number_win.show()

    def closeEvent(self, event):
        """重写该方法主要是解决打开子窗口时，如果关闭了主窗口但子窗口仍显示的问题，使用sys.exit(0) 时就会只要关闭了主窗口，所有关联的子窗口也会全部关闭"""
        sys.exit(0)  # 关闭登录窗口的时候，注册窗口也应该关闭


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
