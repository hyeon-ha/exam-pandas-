import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_window = uic.loadUiType('./poster_view.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_squidgame.clicked.connect(self.btn_clicked_slot)
        self.btn_mogadishu.clicked.connect(self.btn_clicked_slot)
        self.btn_moonlight.clicked.connect(self.btn_clicked_slot)
        self.btn_dongju.clicked.connect(self.btn_clicked_slot)

    def btn_clicked_slot(self):

        self.lbl_dongju.hide()
        self.lbl_moonlight.hide()
        self.lbl_mogadishu.hide()
        self.lbl_squidgame.hide()
        btn = self.sender()
        if btn.objectName() == 'btn_squidgame':
            self.lbl_squidgame.show()
        elif btn.objectName() == 'btn_mogadishu':
            self.lbl_mogadishu.show()
        elif btn.objectName() == 'btn_moonlight':
            self.lbl_moonlight.show()
        elif btn.objectName() == 'btn_dongju':
            self.lbl_dongju.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())