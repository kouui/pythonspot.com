"""
https://pythonspot.com/en/pyqt5/

9. PyQt5 table
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout

class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 200

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable(4, 3)

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # show widget
        self.show()

    def createTable(self, nrows, ncols):

        self.tableWidget = QTableWidget(nrows, ncols)
        # self.tableWidget.setRowCount(nrows)
        # self.tableWidget.setColumnCount(ncols)

        for i in range(nrows):
            for j in range(ncols):
                self.tableWidget.setItem(i,j, QTableWidgetItem("Cell ({},{})".format(i, j)) )

        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
