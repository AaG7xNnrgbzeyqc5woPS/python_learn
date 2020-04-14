import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import hello_world

def click_success():
    print("哈哈哈，我终于成功了！")
    print("我的第一个PyQT程序！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_world.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(click_success)
    sys.exit(app.exec_())

    