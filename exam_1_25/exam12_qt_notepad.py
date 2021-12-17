import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window = uic.loadUiType('./qt_notepad.ui')[0]

class Exam(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path = ('제목 없음', '')
        self.title = self.path[0] + ' - Qt Note Pad'
        self.edited_flag = False
        self.setWindowTitle(self.title)
        self.actionSave_as.triggered.connect(
            self.action_save_as_slot)
        self.actionSave.triggered.connect(
            self.action_save_slot)
        self.actionOpen.triggered.connect(
            self.action_open_slot )
        self.actionNew.triggered.connect(
            self.action_new_slot)
        self.plainTextEdit.textChanged.connect(
            self.text_changed_slot)
        self.actionUndo.triggered.connect(
            self.plainTextEdit.undo)
        self.actionRedo.triggered.connect(
            self.plainTextEdit.redo)
        self.actionCut.triggered.connect(
            self.plainTextEdit.cut)
        self.actionCopy.triggered.connect(
            self.plainTextEdit.copy)
        self.actionPaste.triggered.connect(
            self.plainTextEdit.paste)
        self.actionDelete.triggered.connect(
            self.plainTextEdit.cut)
        self.actionFont.triggered.connect(
            self.action_font_slot)
        self.actionAbout.triggered.connect(
            self.action_about_slot )

    def action_about_slot(self):
        QMessageBox.about(self,
                'PyQt Note Pad',
                '''
                만든이 : ABC Lab
                버전 정보 : 1.0.0
                ''')

    def action_font_slot(self):
        font = QFontDialog.getFont()
        if font[1]:
            self.plainTextEdit.setFont(font[0])

    def new_file_init(self):
        self.plainTextEdit.setPlainText('')
        self.path = ('제목 없음', '')
        self.plainTextEdit_init()

    def action_new_slot(self):
        if self.edited_flag:
            ans = QMessageBox.question(self,
                   '저장하기', '저장할까요?',
                   QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                   QMessageBox.Yes)
            if ans == QMessageBox.Yes:
                if not self.action_save_slot():
                    self.new_file_init()
            elif ans == QMessageBox.No:
                self.new_file_init()
        else:
            self.new_file_init()

    def text_changed_slot(self):
        self.edited_flag = True
        self.plainTextEdit.textChanged.disconnect(
            self.text_changed_slot)
        self.setWindowTitle('*' + self.title)
        print(self.edited_flag)

    def closeEvent(self, QCloseEvent):
        if self.edited_flag:
            ans = QMessageBox.question(self,
                '저장하기', '저장할까요?',
                QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                QMessageBox.Yes)
            if ans == QMessageBox.Yes:
                if self.action_save_slot():
                    QCloseEvent.ignore()
                else:
                    QCloseEvent.accept()
            elif ans == QMessageBox.No:
                QCloseEvent.accept()
            else : QCloseEvent.ignore()
        else : QCloseEvent.accept()

    def set_title(self):
        self.title = self.path[0].split('/')[-1] + ' - Qt Note Pad'
        self.setWindowTitle(self.title)

    def plainTextEdit_init(self):
        self.edited_flag = False
        self.set_title()
        self.plainTextEdit.textChanged.connect(
            self.text_changed_slot)

    def action_open_slot(self):
        if self.edited_flag:
            ans = QMessageBox.question(self,
                   '저장하기', '저장할까요?',
                   QMessageBox.No | QMessageBox.Cancel | QMessageBox.Yes,
                   QMessageBox.Yes)
            if ans == QMessageBox.Yes:
                self.action_save_slot()

        old_path = self.path
        self.path = QFileDialog.getOpenFileName(
            self, 'Save file', '',
            'Text Files(*.txt);;Python Files(*.py);;All Files(*.*)')
        print(self.path)
        if self.path[0] != '':

            with open(self.path[0], 'r') as f:
                str_read = f.read()
            self.plainTextEdit.setPlainText(str_read)
            self.plainTextEdit_init()
        else: self.path = old_path


    def action_save_slot(self):
        if self.path[0] != '제목 없음':
            with open(self.path[0], 'w') as f:
                f.write(self.plainTextEdit.toPlainText())
            self.plainTextEdit_init()
            return 0
        else:
            return self.action_save_as_slot()


    def action_save_as_slot(self):
        old_path = self.path
        self.path = QFileDialog.getSaveFileName(
            self, 'Save file', '',
            'Text Files(*.txt);;Python Files(*.py);;All Files(*.*)'
        )
        if self.path[0] != '':
            with open(self.path[0], 'w') as f:
                f.write(self.plainTextEdit.toPlainText())
            self.plainTextEdit_init()
            return 0
        else:
            self.path = old_path
            return -1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())