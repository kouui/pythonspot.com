"""
https://pythonspot.com/en/pyqt5/

15. PyQt5 image
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create widget
        label = QLabel(self)
        pixmap = QPixmap("./image.png")
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
