#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStackedWidget, QWidget, QGridLayout, QLabel, \
    QDoubleSpinBox, QHBoxLayout, QSpinBox, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon, QAction, QFont, Qt


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

        self.subtract_inputs1 = []
        self.subtract_inputs2 = []
        self.subtract_result = []

        self.times_scalar = None
        self.times_inputs = []
        self.times_result = []

        self.timem_inputs1 = []
        self.timem_inputs2 = []
        self.timem_result = []

        self.transpose_inputs = []
        self.transpose_result = []

        self.det_inputs = []
        self.det_result = None

        self.reverse_inputs = []
        self.reverse_result = []

        self.trace_inputs = []
        self.trace_result = None

        #Toolbar
        toolbar = QToolBar("Toolbar")
        toolbar.setFont(QFont("Courier New", 12))
        self.addToolBar(toolbar)

        add_view_option = QAction("+", self)
        subtract_view_option = QAction("-", self)
        timesk_view_option = QAction("s*", self)
        timesm_view_option = QAction("M*", self)
        transpose_view_option = QAction("T", self)
        det_view_option = QAction("|m|", self)
        reverse_view_option = QAction("^-1", self)
        power_view_option = QAction("^s", self)
        trace_view_option = QAction("Tr", self)
        cofactor_view_option = QAction("Co", self)
        unit_view_option = QAction("I", self)

        toolbar.addAction(add_view_option)
        toolbar.addAction(subtract_view_option)
        toolbar.addAction(timesk_view_option)
        toolbar.addAction(timesm_view_option)
        toolbar.addAction(transpose_view_option)
        toolbar.addAction(det_view_option)
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


        self.stack.addWidget(self.__gen_add_view())
        self.stack.addWidget(self.__gen_subtract_view())
        self.stack.addWidget(self.__gen_times_view())
        self.stack.addWidget(self.__gen_timem_view())
        self.stack.addWidget(self.__gen_transpose_view())
        self.stack.addWidget(self.__gen_det_view())
        self.stack.addWidget(self.__gen_reverse_view())
        self.stack.addWidget(QWidget())
        self.stack.addWidget(self.__gen_trace_view())
        self.setCentralWidget(self.stack)

        #Toolbar connection
        add_view_option.triggered.connect(lambda: self.__change_refresh_view(0, self.rows1, self.cols1, self.rows2, self.cols2))
        subtract_view_option.triggered.connect(lambda: self.__change_refresh_view(1, self.rows1, self.cols1, self.rows2, self.cols2))
        timesk_view_option.triggered.connect(lambda: self.__change_refresh_view(2, self.rows1, self.cols1, self.rows2, self.cols2))
        timesm_view_option.triggered.connect(lambda: self.__change_refresh_view(3, self.rows1, self.cols1, self.rows2, self.cols2))
        transpose_view_option.triggered.connect(lambda: self.__change_refresh_view(4, self.rows1, self.cols1, self.rows2, self.cols2))
        det_view_option.triggered.connect(lambda: self.__change_refresh_view(5, self.rows1, self.cols1, self.rows2, self.cols2))
        reverse_view_option.triggered.connect(lambda: self.__change_refresh_view(6, self.rows1, self.cols1, self.rows2, self.cols2))

        trace_view_option.triggered.connect(lambda: self.__change_refresh_view(8, self.rows1, self.cols1, self.rows2, self.cols2))

        #Initialisation
        self.setWindowTitle("Matrix Calculator")
        self.resize(1024, 576)
        self.setWindowIcon(QIcon("icons/icon.png"))


    def __gen_add_view(self) -> QWidget:
        add_view = QWidget()
        add_view.setContentsMargins(25, 25, 25, 25)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(0, rows_input.value(), cols_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(0, rows_input.value(), cols_input.value()))
        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        add_input1 = self.generate_input_grid(self.rows1, self.cols1, self.add_inputs1)
        h_layout.addWidget(add_input1, 5)

        plus_label = QLabel("+")
        plus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        plus_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(plus_label)

        add_input2 = self.generate_input_grid(self.rows1, self.cols1, self.add_inputs2)
        h_layout.addWidget(add_input2, 5)

        eq_label = QLabel("=")
        eq_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        eq_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(eq_label)

        add_result = self.generate_input_grid(self.rows1, self.cols1, self.add_result, True)
        h_layout.addWidget(add_result, 5)

        v_layout.addWidget(main_area, 5)

        add_button = QPushButton("Add")
        add_button.setFixedSize(250, 50)
        add_button.setFont(QFont("Courier New", 25))
        add_button.setCursor(Qt.CursorShape.PointingHandCursor)
        add_button.clicked.connect(lambda: print(self.add_result))

        v_layout.addWidget(add_button, alignment = Qt.AlignmentFlag.AlignCenter)

        return add_view

    def __gen_subtract_view(self) -> QWidget:
        subtract_view = QWidget()
        subtract_view.setContentsMargins(25, 25, 25, 25)

        v_layout = QVBoxLayout(subtract_view)
        subtract_view.setLayout(v_layout)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(1, rows_input.value(), cols_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(1, rows_input.value(), cols_input.value()))
        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        subtract_input1 = self.generate_input_grid(self.rows1, self.cols1, self.add_inputs1)
        h_layout.addWidget(subtract_input1, 5)

        minus_label = QLabel("-")
        minus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        minus_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(minus_label)

        subtract_input2 = self.generate_input_grid(self.rows1, self.cols1, self.add_inputs2)
        h_layout.addWidget(subtract_input2, 5)

        eq_label = QLabel("=")
        eq_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        eq_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(eq_label)

        subtract_result = self.generate_input_grid(self.rows1, self.cols1, self.subtract_result, True)
        h_layout.addWidget(subtract_result, 5)

        v_layout.addWidget(main_area, 5)

        subtract_button = QPushButton("Subtract")
        subtract_button.setFixedSize(250, 50)
        subtract_button.setFont(QFont("Courier New", 25))
        subtract_button.setCursor(Qt.CursorShape.PointingHandCursor)
        subtract_button.clicked.connect(lambda: print(self.subtract_result))

        v_layout.addWidget(subtract_button, alignment = Qt.AlignmentFlag.AlignCenter)

        return subtract_view

    def __gen_times_view(self) -> QWidget:
        times_view = QWidget()
        times_view.setContentsMargins(25, 25, 25, 25)
        
        v_layout = QVBoxLayout(times_view)
        times_view.setLayout(v_layout)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(2, rows_input.value(), cols_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(2, rows_input.value(), cols_input.value()))


        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        s_input = QDoubleSpinBox()
        s_input.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        s_input.setFixedSize(65, 25)
        s_input.setSingleStep(0.1)
        s_input.setDecimals(4)
        s_input.setRange(-9999, 9999)
        s_input.setValue(0.0)
        s_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.times_scalar = s_input

        h_layout.addWidget(s_input, 5)

        times_label = QLabel("*")
        times_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        times_label.setFont(QFont("Courier New", 30))

        h_layout.addWidget(times_label, 5)

        times_inputs = self.generate_input_grid(self.rows1, self.cols1, self.times_inputs)
        h_layout.addWidget(times_inputs, 5)

        eq_label = QLabel("=")
        eq_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        eq_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(eq_label, 5)

        times_result = self.generate_input_grid(self.rows1, self.cols1, self.times_result, True)
        h_layout.addWidget(times_result, 5)

        v_layout.addWidget(main_area, 5)

        times_button = QPushButton("Multiply")
        times_button.setFixedSize(250, 50)
        times_button.setFont(QFont("Courier New", 25))
        times_button.setCursor(Qt.CursorShape.PointingHandCursor)
        times_button.clicked.connect(lambda: print(self.times_result))

        v_layout.addWidget(times_button, alignment = Qt.AlignmentFlag.AlignCenter)

        return times_view

    def __gen_timem_view(self) -> QWidget:
        self.cols1 = self.rows2

        timem_view = QWidget()
        timem_view.setContentsMargins(25, 25, 25, 25)

        v_layout = QVBoxLayout(timem_view)
        timem_view.setLayout(v_layout)

        header = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setLayout(h_layout)

        size_label = QLabel("Sizes:")
        size_label.setFont(QFont("Courier New", 20))
        size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_layout.addWidget(size_label)

        rows1_input = QSpinBox()
        rows1_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rows1_input.setFixedSize(75, 25)
        rows1_input.lineEdit().setReadOnly(True)
        rows1_input.setRange(1, 5)
        rows1_input.setValue(self.rows1)
        h_layout.addWidget(rows1_input)

        x_label = QLabel("X")
        x_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        x_label.setFont(QFont("Courier New", 12))
        h_layout.addWidget(x_label)

        cols1_input = QSpinBox()
        cols1_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cols1_input.setFixedSize(75, 25)
        cols1_input.lineEdit().setReadOnly(True)
        cols1_input.setRange(1, 5)
        cols1_input.setValue(self.cols1)

        h_layout.addWidget(cols1_input)

        sem_label = QLabel("; ")
        sem_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sem_label.setFont(QFont("Courier New", 12))
        h_layout.addWidget(sem_label)

        rows2_input = QSpinBox()
        rows2_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rows2_input.setFixedSize(75, 25)
        rows2_input.lineEdit().setReadOnly(True)
        rows2_input.setRange(1, 5)
        rows2_input.setValue(self.rows2)
        h_layout.addWidget(rows2_input)

        x_label = QLabel("X")
        x_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        x_label.setFont(QFont("Courier New", 12))
        h_layout.addWidget(x_label)

        cols2_input = QSpinBox()
        cols2_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cols2_input.setFixedSize(75, 25)
        cols2_input.lineEdit().setReadOnly(True)
        cols2_input.setRange(1, 5)
        cols2_input.setValue(self.cols2)

        h_layout.addWidget(cols2_input)

        rows1_input.valueChanged.connect(lambda: self.__change_refresh_view(3, rows1_input.value(), cols1_input.value(), cols1_input.value(), cols2_input.value()))
        cols1_input.valueChanged.connect(lambda: self.__change_refresh_view(3, rows1_input.value(), cols1_input.value(), cols1_input.value(), cols2_input.value()))
        rows2_input.valueChanged.connect(lambda: self.__change_refresh_view(3, rows1_input.value(), rows2_input.value(), rows2_input.value(), cols2_input.value()))
        cols2_input.valueChanged.connect(lambda: self.__change_refresh_view(3, rows1_input.value(), rows2_input.value(), rows2_input.value(), cols2_input.value()))

        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        timem_inputs1 = self.generate_input_grid(self.rows1, self.cols1, self.timem_inputs1)
        h_layout.addWidget(timem_inputs1, 5)

        h_layout.addWidget(timem_inputs1, 5)

        times_label = QLabel("*")
        times_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        times_label.setFont(QFont("Courier New", 30))

        h_layout.addWidget(times_label, 5)

        timem_inputs2 = self.generate_input_grid(self.cols1, self.cols2, self.timem_inputs2)
        h_layout.addWidget(timem_inputs2, 5)

        eq_label = QLabel("=")
        eq_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        eq_label.setFont(QFont("Courier New", 30))
        h_layout.addWidget(eq_label, 5)

        timem_result = self.generate_input_grid(self.rows1, self.cols2, self.timem_result, True)
        h_layout.addWidget(timem_result, 5)

        v_layout.addWidget(main_area, 5)

        timem_button = QPushButton("Multiply")
        timem_button.setFixedSize(250, 50)
        timem_button.setFont(QFont("Courier New", 25))
        timem_button.setCursor(Qt.CursorShape.PointingHandCursor)
        timem_button.clicked.connect(lambda: print(self.timem_result))

        v_layout.addWidget(timem_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return timem_view

    def __gen_transpose_view(self) -> QWidget:
        transpose_view = QWidget()
        transpose_view.setContentsMargins(25, 25, 25, 25)

        v_layout = QVBoxLayout(transpose_view)
        transpose_view.setLayout(v_layout)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(4, rows_input.value(), cols_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(4, rows_input.value(), cols_input.value()))

        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        transpose_inputs = self.generate_input_grid(self.rows1, self.cols1, self.transpose_inputs)
        h_layout.addWidget(transpose_inputs, 5)

        arr_label = QLabel("→")
        arr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        arr_label.setFont(QFont("Courier New", 40))
        h_layout.addWidget(arr_label)

        transpose_result = self.generate_input_grid(self.cols1, self.rows1, self.transpose_result)
        h_layout.addWidget(transpose_result, 5)

        v_layout.addWidget(main_area, 5)

        transpose_button = QPushButton("Transpose")
        transpose_button.setFixedSize(250, 50)
        transpose_button.setFont(QFont("Courier New", 25))
        transpose_button.setCursor(Qt.CursorShape.PointingHandCursor)
        transpose_button.clicked.connect(lambda: print(self.transpose_result))

        v_layout.addWidget(transpose_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return transpose_view

    def __gen_det_view(self) -> QWidget:
        self.cols1 = self.rows1

        det_view = QWidget()
        det_view.setContentsMargins(25, 25, 25, 25)

        v_layout = QVBoxLayout(det_view)
        det_view.setLayout(v_layout)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(5, rows_input.value(), rows_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(5, cols_input.value(), cols_input.value()))

        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        det_inputs = self.generate_input_grid(self.rows1, self.cols1, self.det_inputs)
        h_layout.addWidget(det_inputs, 5)

        arr_label = QLabel("→")
        arr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        arr_label.setFont(QFont("Courier New", 40))
        h_layout.addWidget(arr_label, 5)

        det_result = QDoubleSpinBox()
        det_result.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        det_result.setFixedSize(65, 25)
        det_result.setSingleStep(0.1)
        det_result.setDecimals(4)
        det_result.setRange(-9999, 9999)
        det_result.setValue(0.0)
        det_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.det_result = det_result

        h_layout.addWidget(det_result, 5)

        v_layout.addWidget(main_area, 5)

        det_button = QPushButton("Determinant")
        det_button.setFixedSize(250, 50)
        det_button.setFont(QFont("Courier New", 25))
        det_button.setCursor(Qt.CursorShape.PointingHandCursor)
        det_button.clicked.connect(lambda: print(self.det_result))

        v_layout.addWidget(det_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return det_view
    
    def __gen_reverse_view(self) -> QWidget:
        self.cols1 = self.rows1

        reverse_view = QWidget()
        reverse_view.setContentsMargins(25, 25, 25, 25)

        v_layout = QVBoxLayout(reverse_view)
        reverse_view.setLayout(v_layout)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(6, rows_input.value(), rows_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(6, cols_input.value(), cols_input.value()))

        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        reverse_inputs = self.generate_input_grid(self.rows1, self.cols1, self.reverse_inputs)
        h_layout.addWidget(reverse_inputs, 5)

        arr_label = QLabel("→")
        arr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        arr_label.setFont(QFont("Courier New", 40))
        h_layout.addWidget(arr_label)

        reverse_result = self.generate_input_grid(self.rows1, self.cols1, self.reverse_result)
        h_layout.addWidget(reverse_result, 5)

        v_layout.addWidget(main_area, 5)

        reverse_button = QPushButton("Reverse")
        reverse_button.setFixedSize(250, 50)
        reverse_button.setFont(QFont("Courier New", 25))
        reverse_button.setCursor(Qt.CursorShape.PointingHandCursor)
        reverse_button.clicked.connect(lambda: print(self.reverse_result))

        v_layout.addWidget(reverse_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return reverse_view
    
    def __gen_power_view(self) -> QWidget:
        pass
    
    def __gen_trace_view(self) -> QWidget:
        self.cols1 = self.rows1

        trace_view = QWidget()
        trace_view.setContentsMargins(25, 25, 25, 25)

        v_layout = QVBoxLayout(trace_view)
        trace_view.setLayout(v_layout)

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

        rows_input.valueChanged.connect(lambda: self.__change_refresh_view(8, rows_input.value(), rows_input.value()))
        cols_input.valueChanged.connect(lambda: self.__change_refresh_view(8, cols_input.value(), cols_input.value()))

        v_layout.addWidget(header)

        main_area = QWidget()
        h_layout = QHBoxLayout(header)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_area.setLayout(h_layout)

        trace_inputs = self.generate_input_grid(self.rows1, self.cols1, self.trace_inputs)
        h_layout.addWidget(trace_inputs, 5)

        arr_label = QLabel("→")
        arr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        arr_label.setFont(QFont("Courier New", 40))
        h_layout.addWidget(arr_label, 5)

        trace_result = QDoubleSpinBox()
        trace_result.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
        trace_result.setFixedSize(65, 25)
        trace_result.setSingleStep(0.1)
        trace_result.setDecimals(4)
        trace_result.setRange(-9999, 9999)
        trace_result.setValue(0.0)
        trace_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trace_result = trace_result

        h_layout.addWidget(trace_result, 5)

        v_layout.addWidget(main_area, 5)

        trace_button = QPushButton("Trace")
        trace_button.setFixedSize(250, 50)
        trace_button.setFont(QFont("Courier New", 25))
        trace_button.setCursor(Qt.CursorShape.PointingHandCursor)
        trace_button.clicked.connect(lambda: print(self.trace_result))

        v_layout.addWidget(trace_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return trace_view

    def __change_refresh_view(self, view_index: int, rows1: int, cols1: int, rows2: int|None = None, cols2: int|None = None) -> None:
        self.rows1 = rows1
        self.cols1 = cols1
        if rows2 is not None:
            self.rows2 = rows2
        if cols2 is not None:
            self.cols2 = cols2

        old_widget = self.stack.widget(view_index)
        if old_widget is not None:
            self.stack.removeWidget(old_widget)
            old_widget.deleteLater()

        match view_index:
            case 0:
                self.stack.insertWidget(view_index, self.__gen_add_view())
            case 1:
                self.stack.insertWidget(view_index, self.__gen_subtract_view())
            case 2:
                self.stack.insertWidget(view_index, self.__gen_times_view())
            case 3:
                self.stack.insertWidget(view_index, self.__gen_timem_view())
            case 4:
                self.stack.insertWidget(view_index, self.__gen_transpose_view())
            case 5:
                self.stack.insertWidget(view_index, self.__gen_det_view())
            case 6:
                self.stack.insertWidget(view_index, self.__gen_reverse_view())
            case 8:
                self.stack.insertWidget(view_index, self.__gen_trace_view())
            case _:
                pass

        self.stack.setCurrentIndex(view_index)

    @staticmethod
    def generate_input_grid(rows: int, cols: int, inputs_container: list|None = None, read_only = False) -> QWidget:
        if inputs_container is None:
            inputs_container = []
        inputs_container.clear()
        input_widget = QWidget()
        grid = QGridLayout(input_widget)
        grid.setHorizontalSpacing(5)
        grid.setVerticalSpacing(5)
        input_widget.setLayout(grid)

        for row in range(rows):
            row_input = []
            for col in range(cols):
                m_input = QDoubleSpinBox()
                m_input.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
                m_input.setFixedSize(65, 25)
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

