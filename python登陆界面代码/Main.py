import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main page')
        self.setWindowIcon(QIcon('./IMG/logo.png'))
        self.setFixedSize(1200, 800)
        self.setFont(QFont('Consolas'))
        self.setStyleSheet("background-image: url('./IMG/4.jpg'); background-repeat: no repeat")
        # self.setWindowOpacity(0.9)
        self.set_ui()

    def set_ui(self):
        self.guess_number()

    def guess_number(self):
        number_font = QFont()
        number_font.setFamily('Consolas')
        number_font.setPixelSize(30)

        self.input_number = QLineEdit(self)  # 创建一个输入框
        self.input_number.setFont(number_font)  # 设置输入框里面的字体
        self.input_number.setPlaceholderText("guess_number")  # 设置提示语
        self.input_number.setFixedSize(200, 100)  # 设置输入框的大小
        self.input_number.move(500, 100)  # 设置窗口的位置

        self.determine_button = QPushButton(self)  # 创建一个确定按钮
        self.determine_button.setFixedSize(100, 100)  # 设置确定按钮大小
        self.determine_button.setFont(number_font)  # 设置确定按钮字体
        self.determine_button.move(750, 100)  # 设置确定按钮位置
        self.determine_button.setText('确定')

        self.determine_button.clicked.connect(self.number_text)

    def number_text(self):
        a = self.input_number.text()
        print(a)
        if a:
            if int(a) == 1:
                QMessageBox.information(self, 'Successfully', '恭喜你答对了', QMessageBox.Yes | QMessageBox.No)
            else:
                QMessageBox.information(self, 'Failed', '很遗憾打错了', QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(self, 'Failed', '请输入数字', QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())