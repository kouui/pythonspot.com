"""
https://pythonspot.com/en/pyqt5/

6. PyQt5 textbox
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QAction, QLineEdit, QMessageBox

class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 textbox'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create text box
        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(280,40)

        # create a button in the window
        self.button = QPushButton("Show text", self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):

        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", "You typed: "+textboxValue, QMessageBox.Ok|QMessageBox.No, QMessageBox.No)
        self.textbox.setText("")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
