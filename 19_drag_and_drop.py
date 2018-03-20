"""
https://pythonspot.com/en/pyqt5/

19. PyQt5 drag and drop

Drag text from the input field to the label,
the label will update its text.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel

class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 drag and drop - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        editBox = QLineEdit("Drag this", self)
        editBox.setDragEnabled(True)
        editBox.move(10, 10)
        editBox.resize(100,32)

        button = CustomLabel('Drop here.', self)
        button.move(130,15)

        self.show()

class CustomLabel(QLabel):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
