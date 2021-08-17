from PyQt5.Qt import *
import sys
import random


class GuessNumber(QMainWindow):
    def __init__(self):
        super(GuessNumber, self).__init__()
        self.setWindowTitle('猜游戏')
        self.setWindowIcon(QIcon('./IMG/en.jpg'))
        self.setFixedSize(640, 320)
        self.setFont(QFont('arial'))
        self.setStyleSheet("background-image: url('./IMG/featureimages/0.jpg'); background-repeat: no repeat")
        self.set_ui()
        self.a = random.randint(0,10)

    def set_ui(self):
        self.guess_number()

    def guess_number(self):
        number_font = QFont()
        number_font.setFamily('arial')
        number_font.setPixelSize(15)

        self.input_number = QLineEdit(self)  # 创建一个输入框
        self.input_number.setFont(number_font)  # 设置输入框里面的字体
        self.input_number.setPlaceholderText("请输入0-10之间的数字")  # 设置提示语
        self.input_number.setFixedSize(200, 50)  # 设置输入框的大小
        self.input_number.move(50, 50)  # 设置窗口的位置

        self.determine_button = QPushButton(self)  # 创建一个确定按钮
        self.determine_button.setFixedSize(100, 50)  # 设置确定按钮大小
        self.determine_button.setFont(number_font)  # 设置确定按钮字体
        self.determine_button.move(300, 50)  # 设置确定按钮位置
        self.determine_button.setText('确定')

        self.determine_button.clicked.connect(self.number_text)

    def number_text(self):
        a = self.input_number.text()
        if a:
            print(self.a)
            if int(a) == self.a:
                QMessageBox.information(self, 'Successfully', '恭喜你答对了', QMessageBox.Yes | QMessageBox.No)
            else:
                QMessageBox.information(self, 'Failed', '很遗憾打错了', QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(self, 'Failed', '请输入数字', QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = GuessNumber()
    run.show()
    sys.exit(app.exec_())