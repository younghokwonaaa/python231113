#DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

#폼클래스 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")


#직접 모듈을 실행한 경우면 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
    