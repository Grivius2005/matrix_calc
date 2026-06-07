#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStackedWidget, QWidget, QGridLayout, QLabel, \
    QDoubleSpinBox, QHBoxLayout, QSpinBox, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon, QAction, QFont, Qt, QGuiApplication


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        #Fields
        self.rows1 = 3
        self.rows2 = 3
        self.cols1 = 3
        self.cols2 = 3

        self.add_inputs1 = []
        self.add_inputs2 = []
        self.add_result = []

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

        self.test_widget2 = QWidget()
        grid2 = QGridLayout(self.test_widget2)

        grid2.addWidget(QLabel("Test view 2"), 0,0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.test_widget2.setLayout(grid2)

        self.stack.addWidget(self.__gen_add_view())
        self.stack.addWidget(self.test_widget2)
        self.stack.addWidget(self.generate_input_grid(3, 3, []))
        self.setCentralWidget(self.stack)

        #Toolbar connection
        add_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        substract_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(1))
        timesk_view_option.triggered.connect(lambda: self.stack.setCurrentIndex(2))

        #Initialisation
        self.setWindowTitle("Matrix Calculator")
        self.resize(1024, 576)
        self.setWindowIcon(QIcon("icons/icon.png"))


    def __gen_add_view(self) -> QWidget:
        add_view = QWidget()
        add_view.setContentsMargins(75, 75, 75, 75)

        v_layout = QVBoxLayout(add_view)
        add_view.setLayout(v_layout)

        header = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setLayout(h_layout)

        size_label = QLabel("Size:")
        size_label.setFont(QFont("Courier New", 20))
        size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_layout.addWidget(size_label)

        rows_input = QSpinBox()
        rows_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rows_input.setFixedSize(75, 25)
        rows_input.lineEdit().setReadOnly(True)
        rows_input.setRange(1, 5)
        rows_input.setValue(self.rows1)
        h_layout.addWidget(rows_input)

        x_label = QLabel("X")
        x_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        x_label.setFont(QFont("Courier New", 12))
        h_layout.addWidget(x_label)

        cols_input = QSpinBox()
        cols_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cols_input.setFixedSize(75, 25)
        cols_input.lineEdit().setReadOnly(True)
        cols_input.setRange(1, 5)
        cols_input.setValue(self.cols1)
        h_layout.addWidget(cols_input)

        v_layout.addWidget(header, 1)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        add_input1 = self.generate_input_grid(self.rows1, self.cols1, self.add_inputs1)
        h_layout.addWidget(add_input1, 5)

        plus_label = QLabel("+")
        plus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        plus_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(plus_label, 1)

        add_input2 = self.generate_input_grid(self.rows1, self.cols1, self.add_inputs2)
        h_layout.addWidget(add_input2, 5)

        eq_label = QLabel("=")
        eq_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        eq_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(eq_label, 1)

        add_result = self.generate_input_grid(self.rows1, self.cols1, self.add_result, True)
        h_layout.addWidget(add_result, 5)

        v_layout.addWidget(main_area, 5)

        add_button = QPushButton("Add")
        add_button.setFixedWidth(200)
        add_button.setCursor(Qt.CursorShape.PointingHandCursor)


        v_layout.addWidget(add_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return add_view


    @staticmethod
    def generate_input_grid(rows: int, cols: int, inputs_container = None, read_only = False) -> QWidget:
        if inputs_container is None:
            inputs_container = []
        input_widget = QWidget()
        grid = QGridLayout(input_widget)
        grid.setHorizontalSpacing(25)
        grid.setVerticalSpacing(25)
        input_widget.setLayout(grid)

        for row in range(rows):
            row_input = []
            for col in range(cols):
                m_input = QDoubleSpinBox()
                m_input.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
                m_input.setFixedSize(75, 25)
                m_input.setSingleStep(0.1)
                m_input.setDecimals(4)
                m_input.setRange(-9999, 9999)
                m_input.setValue(0.0)
                m_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

                if read_only:
                    m_input.setReadOnly(True)
                row_input.append(m_input)
                grid.addWidget(m_input, row, col)
            inputs_container.append(row_input)
        return input_widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

