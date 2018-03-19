
"""
https://pythonspot.com/en/pyqt5/

3. PyQt5 buttons
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        # add statusbar
        self.statusBar().showMessage("message from statusbar!")

        # add button
        button = QPushButton("button", self)
            # The method setToolTip shows the message
            # when the user points the mouse on the button.
        button.setToolTip("This is an example button")
            # the button is moved to the coordinates x=100,y=70
        button.move(100, 70)
            # Add connect the method to the click
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.statusBar().showMessage("button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
