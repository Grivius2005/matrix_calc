#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStackedWidget, QWidget, QGridLayout, QLabel
from PySide6.QtGui import QIcon, QAction, QFont, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Toolbar
        toolbar = QToolBar("Toolbar")
        toolbar.setFont(QFont("Courier New", 12))
        self.addToolBar(toolbar)

        add_view_option = QAction("+", self)
        substract_view_option = QAction("-", self)
        timesk_view_option = QAction("s*", self)
        timesm_view_option = QAction("M*", self)
        transpose_view_option = QAction("Tr", self)
        reverse_view_option = QAction("^-1", self)
        power_view_option = QAction("^s", self)
        trace_view_option = QAction("Tc", self)
        cofactor_view_option = QAction("Co", self)
        unit_view_option = QAction("I", self)

        toolbar.addAction(add_view_option)
        toolbar.addAction(substract_view_option)
        toolbar.addAction(timesk_view_option)
        toolbar.addAction(timesm_view_option)
        toolbar.addAction(transpose_view_option)
        toolbar.addAction(reverse_view_option)
        toolbar.addAction(power_view_option)
        toolbar.addAction(trace_view_option)
        toolbar.addAction(cofactor_view_option)
        toolbar.addAction(unit_view_option)

        for action in toolbar.actions():
            widget = toolbar.widgetForAction(action)
            if widget:
                widget.setCursor(Qt.CursorShape.PointingHandCursor)

        #StackWidget
        self.stack = QStackedWidget()

        self.test_widget1 = QWidget()
        self.test_widget2 = QWidget()
        grid1 = QGridLayout()
        grid2 = QGridLayout()

        grid1.addWidget(QLabel("Test view 1"), 0,0, alignment=Qt.AlignmentFlag.AlignCenter)
        grid2.addWidget(QLabel("Test view 2"), 0,0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.test_widget1.setLayout(grid1)
        self.test_widget2.setLayout(grid2)

        self.stack.addWidget(self.test_widget1)
        self.stack.addWidget(self.test_widget2)
        self.setCentralWidget(self.stack)

        #Toolbar connection
        add_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        substract_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(1))

        #Initialisation
        self.setWindowTitle("Matrix Calculator")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon("icons/icon.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

