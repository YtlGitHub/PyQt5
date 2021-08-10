# 导入QApplication -> 应用程序，一个程序只能有一个应用程序接口
# 导入QMainWindow -> 主窗口，一个程序也只能有一个主窗口
from PyQt5.Qt import *
# sys -> 获取系统的信息，比如命令行的，并且承担关闭窗口后完全退出的责任
import sys
from Sign_Up import SignWindow
from Database import Database


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.icon = QIcon("./IMG/logo.png")  # 图标
        self.database = Database('./data.db')  # 数据路径
        self.sign_up_win = SignWindow  # 创建的注册窗口
        # self.resize(1000, 800)  # resize -> 设置窗口的大小
        self.setFixedSize(1000, 700)  # setFixedSize 固定窗口大小
        self.setWindowTitle('Login in')  # setWindowTitle -> 设置窗口的标题
        self.set_ui()

    def set_ui(self):
        self.set_background_image()
        self.change_icon()
        self.add_label()
        self.add_line_edit()
        self.add_button()

    def change_icon(self):
        """用来修改图像的图标"""
        self.setWindowIcon(self.icon)

    def set_background_image(self):
        """添加背景图片"""
        self.frame = QFrame(self)
        self.frame.resize(1000, 700)
        self.frame.move(0, 0)
        self.frame.setStyleSheet('background-image: url("./IMG/1.jpg"); background-repeat: no-repeat; text-align:center;')

    def add_label(self):
        # 我们来设置以下字体，利用 QFont对象来创建一个字体对象，然后使用QLabel对象的setFont方法进行设置
        # 设置字体
        label_font = QFont()  # QFont中的方法3：
        label_font.setFamily('Consolas')  # setFamily -> 设置字体
        label_font.setPixelSize(35)  # setPixelSize -> 设置字体大小

        self.username_label = QLabel(self)  # 在上述代码中，我们首先定义了一个QLabel对象，然后使用其中的方法3
        self.password_label = QLabel(self)  # 创建文本标签
        self.cyberits_label = QLabel(self)  # 创建文本标签
        self.username_label.setText('username')  # setText -> 设置文本内容
        self.password_label.setText('password')  # 设置标签中的文本
        self.cyberits_label.setText('Welcome to the login interface of Ytl')  # 设置标签中的文本
        self.username_label.setFixedSize(240, 40)  # setFixedSize -> 设置不可修改的窗口大小
        self.password_label.setFixedSize(240, 40)  # 设置标签的大小
        self.cyberits_label.setFixedSize(700, 40)  # 设置标签大小
        self.username_label.move(120, 530)  # 设置文本位置
        self.password_label.move(120, 600)  # 设置文本位置
        self.cyberits_label.move(150, 100)  # 设置文本位置
        self.username_label.setFont(label_font)  # 设置字体样式
        self.password_label.setFont(label_font)  # 设置字体样式
        self.cyberits_label.setFont(label_font)  # 设置字体样式

    def add_line_edit(self):
        """添加输入框"""
        line_edit_font = QFont()
        line_edit_font.setFamily('Consolas')
        line_edit_font.setPixelSize(30)

        # 创建
        self.username_edit = QLineEdit(self)  # QLineEdit -> 定义一个输入框对象
        self.password_edit = QLineEdit(self)

        # 设置密码格式
        self.password_edit.setEchoMode(QLineEdit.Password)  # setEchoMode(QLineEdit.Password)-> 设置输入的时候显示的为我们平常所见的小圆点，无法看到其中的文本内容

        # 设置字体
        self.username_edit.setFont(line_edit_font)
        self.password_edit.setFont(line_edit_font)

        # 设置占位符，相当于提示信息
        self.username_edit.setPlaceholderText("username")
        self.password_edit.setPlaceholderText("password")

        # 设置大小
        self.username_edit.setFixedSize(350, 40)
        self.password_edit.setFixedSize(350, 40)

        # 设置位置
        self.username_edit.move(320, 530)
        self.password_edit.move(320, 600)

    def add_button(self):
        """添加按钮"""
        button_font = QFont()
        button_font.setFamily('Consolas')
        button_font.setPixelSize(30)

        # 创建按钮对象
        self.login_button = QPushButton("Login", self)
        self.sign_button = QPushButton(self)

        # 修改大小且不可变
        self.login_button.setFixedSize(160, 50)
        self.sign_button.setFixedSize(160, 50)

        # 设置字体
        self.login_button.setFont(button_font)
        self.sign_button.setFont(button_font)

        # 设置位置
        self.login_button.move(750, 530)
        self.sign_button.move(750, 600)

        # 设置文本提示内容
        self.login_button.setText("Login in")
        self.sign_button.setText("Sign up")

        # 实现功能，按钮点击之后执行的动作
        self.login_button.clicked.connect(self.login)
        self.sign_button.clicked.connect(self.sign_up_window)

    def login(self):
        """登录功能实现"""
        username = self.username_edit.text()
        password = self.password_edit.text()
        data = self.database.find_password_by_username(username)  # 在数据库中查找数据
        print(data)
        if username and password:  # 如果两个输入框都不为空
            if data:
                if str(data[0][0]) == password:
                    QMessageBox.information(self, 'Successfully', 'Login in successful \n Welcome {}'.format(username), QMessageBox.Yes | QMessageBox.No)
                    self.password_edit.setText('')  # 登录成功，将之前的用户信息清除
                    self.username_edit.setText('')
                    self.close()
                    if username == 'admin':  # 如果是管理员，进入管理界面
                        self.admin_win.show()
                    else:
                        self.main_win.show()  # 如果不是进入客户管理界面

                else:
                    QMessageBox.information(self, 'Failed', 'Password is wrong, try again', QMessageBox.Yes | QMessageBox.No)
            else:
                QMessageBox.information(self, 'Error', 'No such username', QMessageBox.Yes | QMessageBox.No)
        elif username:  # 如果用户名写了
            QMessageBox.information(self, 'Error', 'Input your password', QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(self, 'Error', 'Fill in the blank', QMessageBox.Yes | QMessageBox.No)

    def sign_up_window(self):
        self.sign_up_win.setWindowIcon(self.icon)
        self.sign_up_win.move(self.x() + 100, self.y() + 100)  # 移动一下注册窗口，以免和之前的重复
        frame = QFrame(self.sign_up_win)
        self.sign_up_win.setWindowFlag(Qt.Dialog)
        frame.resize(1000, 300)
        frame.setStyleSheet('background-image: url("./IMG/python.png"); background-repeat: no-repeat;')
        frame.move(40, 150)
        # 打开注册窗口时，清除原来的信息
        self.password_edit.setText('')
        self.username_edit.setText('')
        self.sign_up_win.show()

    def closeEvent(self, event):
        self.sign_up_win.close()  # 关闭登录窗口的时候，注册窗口也应该关闭


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用
    # 创建一个窗口window并且调用show方法来显示窗口2
    window = MyWindow()
    window.show()
    # app.exec_() 可以让窗口一直运行知道被关闭，类似于tkinter中的mainloop方法
    # sys.exit(app.exec_())可以用来判断程序是否正常退出
    sys.exit(app.exec_())

