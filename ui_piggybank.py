# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'piggybankhPlcmU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

cwd=os.getcwd()
cwd=cwd.replace("\\","/")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"background-color: rgb(162, 103, 172);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_pg = QWidget()
        self.main_pg.setObjectName(u"main_pg")
        self.break_btn = QPushButton(self.main_pg)
        self.break_btn.setObjectName(u"break_btn")
        self.break_btn.setGeometry(QRect(1300, 850, 496, 106))
        self.break_btn.setStyleSheet(u"font: 56pt \"Calibri\";\n"
"background-color: rgb(206, 123, 176);\n"
"color:rgb(255, 188, 209);\n"
"border-radius: 20px;\n"
"")
        self.add_btn = QPushButton(self.main_pg)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(714, 672, 492, 96))
        self.add_btn.setStyleSheet(u"font: 56pt \"Calibri\";\n"
"background-color: rgb(206, 123, 176);\n"
"color:rgb(255, 188, 209);\n"
"border-radius: 20px;\n"
"")
        self.money_edit = QLineEdit(self.main_pg)
        self.money_edit.setObjectName(u"money_edit")
        self.money_edit.setGeometry(QRect(620, 550, 680, 106))
        self.money_edit.setStyleSheet(u"font: 70pt \"Calibri\";\n"
"color:rgb(255, 188, 209);\n"
"border-radius: 20px;\n"
"background-color: rgb(206, 123, 176);")
        self.money_edit.setAlignment(Qt.AlignCenter)
        self.piggy_icon = QLabel(self.main_pg)
        self.piggy_icon.setObjectName(u"piggy_icon")
        self.piggy_icon.setGeometry(QRect(804, 155, 312, 312))
        self.piggy_icon.setStyleSheet(u"image: url("+cwd+"/piggy.png) no-repeat center center fixed;\n"
"")
        self.stackedWidget.addWidget(self.main_pg)
        self.savings_pg = QWidget()
        self.savings_pg.setObjectName(u"savings_pg")
        self.savings_label = QLabel(self.savings_pg)
        self.savings_label.setObjectName(u"savings_label")
        self.savings_label.setGeometry(QRect(690, 300, 664, 158))
        self.savings_label.setStyleSheet(u"font: 100pt \"Calibri\";\n"
"color:rgb(255, 188, 209);")
        self.money_label = QLabel(self.savings_pg)
        self.money_label.setObjectName(u"money_label")
        self.money_label.setGeometry(QRect(690, 496, 664, 175))
        self.money_label.setStyleSheet(u"font: 100pt \"Calibri\";\n"
"color:rgb(255, 188, 209);")
        self.money_label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.savings_pg)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.break_btn.setText(QCoreApplication.translate("MainWindow", u"Break", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))

        self.money_edit.setPlaceholderText("Money")
        self.piggy_icon.setText("")
        self.savings_label.setText(QCoreApplication.translate("MainWindow", u"Your savings", None))
        self.money_label.setText(QCoreApplication.translate("MainWindow", u"____", None))
    # retranslateUi

