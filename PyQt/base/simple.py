#!/usr/bin/python3
#_*_ coding: utf-8 _*_

"""
Py40.com PyQt5 turarial

"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,250)
    w.move(300,300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())




