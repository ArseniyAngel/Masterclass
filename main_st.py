import sys

from PyQt6 import QtWidgets

from start_window_st import StartWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
