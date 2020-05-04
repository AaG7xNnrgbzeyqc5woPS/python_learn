#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
This program centers a window on the screen.
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150) #通过修改参数测试，可以明白前面一个参数是窗口（QWidget）的宽度，后面一个高度
        self.center()

        self.setWindowTitle('Center')
        self.show()

    #控制窗口显示在屏幕中心的方法
    def center(self):
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    #测试OK



        