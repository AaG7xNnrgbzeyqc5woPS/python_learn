# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_world.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTree = QtWidgets.QMenu(self.menuFile)
        self.menuTree.setObjectName("menuTree")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSubtree = QtWidgets.QAction(MainWindow)
        self.actionSubtree.setObjectName("actionSubtree")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionText = QtWidgets.QAction(MainWindow)
        self.actionText.setObjectName("actionText")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuTree.addAction(self.actionSubtree)
        self.menuTree.addAction(self.actionClose)
        self.menuTree.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionEdit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuTree.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionText)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow_fixed"))
        self.label.setText(_translate("MainWindow", "Hello World!！"))
        self.pushButton.setText(_translate("MainWindow", "HelloWord"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTree.setTitle(_translate("MainWindow", "Tree"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSubtree.setText(_translate("MainWindow", "Subtree"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As ..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionText.setText(_translate("MainWindow", "Text"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
