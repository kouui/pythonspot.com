"""
https://pythonspot.com/en/pyqt5/

12. PyQt5 grid layout
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout

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

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):

        self.horizontalGroupBox = QGroupBox("Grid")

        layout = QGridLayout()
        #layout.setColumnStretch(1, 4)
        #layout.setColumnStretch(2, 4)

        for i in range(3):
            for j in range(1,4):
                layout.addWidget(QPushButton("{}".format(i*3+j)), i, j)


        self.horizontalGroupBox.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
