"""
https://pythonspot.com/en/pyqt5/

11. PyQt5 horizontal layout
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QGroupBox, QDialog, QVBoxLayout

class Test(QDialog):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):

        self.horizontalGroupBox = QGroupBox("What is your favorite color?")
        layout = QHBoxLayout()

        buttonColordict = {}
        for color in ["Blue", "Red", "Green"]:
            buttonColordict[color] = QPushButton(color)
            buttonColordict[color].clicked.connect(self.on_click)
            layout.addWidget(buttonColordict[color])

        self.horizontalGroupBox.setLayout(layout)

    def on_click(self):

        button = self.sender()
        """
        http://yu00.hatenablog.com/entry/2015/09/14/202729
        """

        print("Pyqt5 button {} clicked".format(button.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
