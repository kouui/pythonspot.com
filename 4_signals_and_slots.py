
"""
https://pythonspot.com/en/pyqt5/

4. PyQt5 signals and slots
"""

import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)

class Dialog(QDialog):

    def __init__(self):
        super(QDialog, self).__init__()

        button = QPushButton("Click")
        button.clicked.connect(self.slot_method)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)

        self.show()

    def slot_method(self):

        print("slot method called.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(app.exec_())
