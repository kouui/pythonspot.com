"""
https://pythonspot.com/en/pyqt5/

17. PyQT5 color dialog
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QColor

class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 color dialog - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton("Open color dialog", self)
        button.setToolTip("Open color dialog")
        # button.move()
        button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(color.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())