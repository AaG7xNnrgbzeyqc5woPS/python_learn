#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)  #关键，connect signal & slot
        #这个例子中展示了一个QtGui.QLCDNumber和QtGui.QSlider。lcd的值会随着滑块的拖动而改变。
        #sld.valueChanged.connect(lcd.display)
        #在这里我们将滚动条的valueChanged信号连接到lcd的display插槽。
        #sender是发出信号的对象。receiver是接收信号的对象。slot(插槽)是对信号做出反应的方法。

        self.setGeometry(800, 300, 550, 550)
         #经过实验四个参数含义如下，(x,y,width,high)
         #原点屏幕左上角，x=横坐标，Y=纵坐标，width=窗体的宽度，high窗体的高度
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#测试，拖动滑动条，显示的LCD数字会变。测试OK
#总结：相关的总结放到上面的注释里面了
#sender是发出信号的对象。receiver是接收信号的对象。slot(插槽)是对信号做出反应的方法。





