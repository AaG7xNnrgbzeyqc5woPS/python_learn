#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
show icon
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QIcon 

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI() #界面绘制交给InitUi方法

    def initUI(self):
        #设置窗口的位置和大小
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        scriptDir = "C:\\Users\\john\\Documents\\python\\python_learn\\PyQt\\base"
        print(scriptDir)
        self.setWindowIcon(QIcon(scriptDir + "\\" +'d1.png')) 
        # 这里有个问题，开始找不到 图标，以为是分辨率或者格式的问题，其实都不是，QT支持 ico,jpg,png等格式图标
        # 问题在于 当然工作目录可能不在 脚本所在的目录，所以找不到图标文件，使用绝对地址就可以了。非常棒！
        # 先简单的这样处理，以后再看看能不能用相对地址，更好的解决这个问题。



        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    #Ok，调试成功，可以显示窗口已经图标
