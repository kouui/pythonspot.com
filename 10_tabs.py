"""
https://pythonspot.com/en/pyqt5/

10. PyQt5 tabs

PyQt5 has a widget to create tabs known as QTabWidget.
The QTabWidget can contain tabs (QWidgets),
which have widgets on them such as labels, buttons, images etcetera.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout

class Test(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 100
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        #--- initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(50,100)

        #--- add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        #--- decorate first tab
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.pushButton1 = QPushButton("Button 1")
        self.tab1_layout.addWidget(self.pushButton1)
        # self.tab1.setLayout(self.tab1_layout)
        """
        if you already `self.tab1_layout = QVBoxLayout(self.tab1)`
        then you do not need to `setLayout` because you have already specified the parent.
        else if you use `self.tab1_layout = QVBoxLayout()` without specifying the parent,
        you need to `setLayout`
        """

        #--- add tabs to widget
        self.layout.addWidget(self.tabs)
        # self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
