"""
https://pythonspot.com/en/pyqt5/

1.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Test(QWidget):

    def __init__(self):
        super().__init__()

        pass

    def initUI(self):

        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
