"""Adicionando PyQT5 em código Python antigo"""

import sys
from validacpf import validate
from geradorcpf import generate
from PyQt5.QtWidgets import QApplication, QMainWindow
from designer_cpf import *

# Refactor do gerador e validador de cpf do mudulo 1 para usar dentro do PyQT5


class NewCpf(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGenerate.clicked.connect(self.generate_cpf)
        self.btnValidate.clicked.connect(self.validate_cpf)

    def generate_cpf(self):
        self.labelReturn.setText(
            str(generate())
        )

    def validate_cpf(self):
        cpf = self.inputValidadeCpf.text()
        self.labelReturn.setText(
            str(validate(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cpf = NewCpf()
    cpf.show()
    qt.exec_()
