#!/usr/bin/python3
#_*_ coding: utf-8 _*_

#在PyQt5中常通过重新实现事件处理器来处理事件。

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event handler')  #事件句柄
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    #vs多行缩进,选中多行，按TAB右移,按shift+TAB左移

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#Test Ok： press Escape key then window close. 



