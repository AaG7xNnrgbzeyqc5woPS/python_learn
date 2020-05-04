#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Event sender')
        self.show()

    #定义事件句柄 Event handler
    def buttonClicked(self):  # self 用来接收事件对象 
        sender = self.sender()  #获取发送事件的的对象
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#test: test is OK!
# press bt1, show some message on status bar
# press bt2, show other message on status bar




