
"""
https://pythonspot.com/en/pyqt5/

5. PyQt5 messagebox
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        #print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel')

        #self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = App()
    sys.exit(app.exec_())
