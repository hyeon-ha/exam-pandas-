import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#리소스 변환 콘솔명령 pyrcc5 calculator.qrc -o calculator_rc.py
form_window = uic.loadUiType('D:\work\python\exam_class\exam-pandas-hh\exam_1_25\calculator.ui')[0]

class Exam(QWidget, form_window):


    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Calculator Ver. 1.0.0')

        self.first_input_flag = True
        self.first_number = 0
        self.opcode = ''
        btn_number_list = [self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4,
                           self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        btn_opcode_list = [self.btn_add, self.btn_sub, self.btn_mul,
                           self.btn_div, self.btn_equal]
        shortcut_opcode = ['+', '-', '*', '/', 'Return']
        # index = 0
        # for btn in btn_number_list:
        #     btn.clicked.connect(self.btn_number_clicked_slot)
        #     btn.setShortcut(str(index))
        #     index += 1
        for index, btn in enumerate(btn_number_list):
            btn.clicked.connect(self.btn_number_clicked_slot)
            btn.setShortcut(str(index))
        for index, btn in enumerate(btn_opcode_list):
            btn.clicked.connect(self.btn_opcode_clicked_slot)
            btn.setShortcut(shortcut_opcode[index])

        # self.btn_0.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_1.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_2.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_3.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_4.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_5.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_6.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_7.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_8.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_9.clicked.connect(self.btn_number_clicked_slot)
        # self.btn_add.clicked.connect(self.btn_opcode_clicked_slot)
        # self.btn_sub.clicked.connect(self.btn_opcode_clicked_slot)
        # self.btn_mul.clicked.connect(self.btn_opcode_clicked_slot)
        # self.btn_div.clicked.connect(self.btn_opcode_clicked_slot)
        # self.btn_equal.clicked.connect(self.btn_opcode_clicked_slot)
        self.btn_clear.clicked.connect(self.btn_clear_clicked_slot)

    def btn_number_clicked_slot(self):
        btn = self.sender()
        if self.first_input_flag:
            self.first_input_flag = False
            self.lbl_result.setText('')
        if self.lbl_result.text() =='0':
            self.lbl_result.setText('')
        str_result = self.lbl_result.text()

        self.lbl_result.setText(str_result + btn.objectName()[4:])

    def btn_opcode_clicked_slot(self):
        if not self.first_input_flag:
            self.first_input_flag = True
            if self.opcode != 'equal':
                self.calculate()
            self.first_number = float(self.lbl_result.text())

        self.opcode = self.sender().objectName()[4:]

    def calculate(self):
        second_number = float(self.lbl_result.text())
        if self.opcode == 'add':
            self.lbl_result.setText(str(self.first_number + second_number))
        elif self.opcode == 'sub':
            self.lbl_result.setText(str(self.first_number - second_number))
        elif self.opcode == 'mul' :
            self.lbl_result.setText(str(self.first_number * second_number))
        elif self.opcode == 'div':
            if second_number:
                self.lbl_result.setText(str(self.first_number / second_number))
            else: self.lbl_result.setText('infinity')


    def btn_clear_clicked_slot(self):
        self.first_input_flag = True
        self.lbl_result.setText('0')
        self.opcode = ''
        self.first_number = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())