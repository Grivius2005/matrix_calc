#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrix Calculator")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon("icons/icon.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

