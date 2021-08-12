from PyQt5.Qt import *
import sys
import webbrowser
import random


class YtlBlog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('YtlBlog')
        self.setWindowIcon(QIcon('./IMG/logo.png'))
        self.label_1 = QLabel(self)
        self.label_1.setText("点击打开YtlBlog博客！<a href='https://ytlgithub.github.io/' style='color:red'>YtlBlog</a>")
        self.label_1.setAutoFillBackground(True)
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, Qt.white)  # 背景颜色
        self.label_1.setPalette(self.palette)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.label_1.setOpenExternalLinks(True)  # 允许访问超链接
        self.label_1.linkHovered.connect(self.link_hovered)  # 针对链接光标略过
        self.label_1.linkActivated.connect(self.link_clicked)  # 针对链接点击事件

        self.label_2 = QLabel(self)
        a = random.randint(0,8)
        self.label_2.setPixmap(QPixmap(f'./IMG/{a}.jpg'))  # 设置图标，与文字冲突，则setText的文字不显示
        self.label_2.mousePressEvent = self.photo_link  # 设置图片点击事件

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.label_1)
        self.vbox.addWidget(self.label_2)
        self.vbox.addStretch()

    def photo_link(self, test):
        webbrowser.open('https://ytlgithub.github.io/')

    def link_hovered(self):
        print("光标滑过Label_1触发事件")

    def link_clicked(self):
        print("点击时触发事件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = YtlBlog()
    win.show()
    sys.exit(app.exec_())