import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from func import *
from ui_piggybank import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.add_btn.clicked.connect(lambda: add(self.ui.money_edit.text()))
        print(self.ui.money_edit.text())
        self.ui.add_btn.clicked.connect(lambda: self.ui.money_edit.setText(""))

        self.ui.break_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.savings_pg))
        self.ui.break_btn.clicked.connect(lambda: self.ui.money_label.setText(savings()))
        self.ui.break_btn.clicked.connect(lambda: clear())
        
        
        
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
