import sys

from mainwindow import mainwindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow()
    app.exec_()