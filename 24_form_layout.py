"""
https://pythonspot.com/en/pyqt5/

24. PyQt5 Form Layout

We create a widget called PlotCanvas that includes the Matplotlib plot.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QFormLayout
from PyQt5.QtWidgets import QLineEdit, QComboBox, QSpinBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QDialogButtonBox

class Test(QDialog):

    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(QDialog, self).__init__()

        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)

        self.show()


    def createFormGroupBox(self):

        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
