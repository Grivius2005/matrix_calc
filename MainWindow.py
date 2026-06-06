#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStackedWidget, QWidget, QGridLayout, QLabel, \
    QDoubleSpinBox, QSpinBox, QAbstractSpinBox
from PySide6.QtGui import QIcon, QAction, QFont, Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
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
        grid1 = QGridLayout(self.test_widget1)
        grid2 = QGridLayout(self.test_widget2)

        grid1.addWidget(QLabel("Test view 1"), 0,0, alignment=Qt.AlignmentFlag.AlignCenter)
        grid2.addWidget(QLabel("Test view 2"), 0,0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.test_widget1.setLayout(grid1)
        self.test_widget2.setLayout(grid2)

        self.stack.addWidget(self.test_widget1)
        self.stack.addWidget(self.test_widget2)
        self.stack.addWidget(self.generate_input_grid(5, 3, []))
        self.setCentralWidget(self.stack)

        #Toolbar connection
        add_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        substract_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(1))
        timesk_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(2))

        #Initialisation
        self.setWindowTitle("Matrix Calculator")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon("icons/icon.png"))

    @staticmethod
    def generate_input_grid(rows: int, cols: int, inputs_container: list[list[QDoubleSpinBox]]) -> QWidget:
        input_widget = QWidget()

        grid = QGridLayout(input_widget)
        input_widget.setLayout(grid)

        for row in range(rows):
            row_input = []
            for col in range(cols):
                m_input = QDoubleSpinBox()
                m_input.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
                m_input.setFixedSize(125, 25)
                m_input.setSingleStep(0.1)
                m_input.setDecimals(4)
                m_input.setRange(-9999, 9999)
                m_input.setValue(0.0)
                row_input.append(m_input)
                grid.addWidget(m_input, row, col)
            inputs_container.append(row_input)
        return input_widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

