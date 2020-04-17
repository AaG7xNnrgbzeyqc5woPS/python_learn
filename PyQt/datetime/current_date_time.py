#！/usr/bin/python3
#QDate, QTime, QDateTime
# http://zetcode.com/gui/pyqt5/datetime/

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print("1: ", now.toString(Qt.ISODate))
print("2: ", now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()
print("3: ", datetime.toString())

time = QTime.currentTime()
print("4: ", time.toString(Qt.DefaultLocaleLongDate))




