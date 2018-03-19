"""
https://pythonspot.com/en/pyqt5/

8. PyQt5 menu
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction

class Test(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        # add this line to show your menubar on your mainwindow, or it will be
        # overlapped by system's menuBar
        # https://qiita.com/void99_/items/50140e367e49ef3a04e6
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")

        newAction = QAction("New", self)
        exitAction = QAction("Exit", self)
        exitAction.setStatusTip("Exit Application")

        saveAction = QAction("Save", self)
        saveAction.setShortcut("Ctrl+S")

        exitAction.triggered.connect(self.close)

        for action in [newAction, saveAction, exitAction]:
            fileMenu.addAction(action)


        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
