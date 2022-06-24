"""Criando uma calculadora com PyQT5"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QLineEdit


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Muda o titulo da janela
        self.setWindowTitle('quasi-scientific calculator')
        # Fixa o tamanho da janela
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # cria uma caixa de digitação
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        # Faz com que a caixa de texto nao seja digitável
        self.display.setDisabled(True)
        # Cor de fundo/ cor fonte/tamanho da fonte
        self.display.setStyleSheet(
            '*{background:white;color:#000;font-size:30px;}'
        )
        # Expande com forme recebe os botoes
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Cria um botão que insere dados no display
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1,
                     lambda: self.display.setText(''),
                     'background:  #d5580d;color:#fff;font-weight: 700')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('<'), 2, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]),
                     'background:  #13823a;color:#fff;font-weight: 700')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1,
                     self.eval_equal,
                     'background:  #095177;color:#fff;font-weight: 700')

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        # Adiciona números ao display
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not function:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text()+btn.text()
                )
            )
        else:
            btn.clicked.connect(function)
        if style:
            btn.setStyleSheet(style)
        btn.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('invalid account')


if __name__ == "__main__":
    # Cria a Janela
    qt = QApplication(sys.argv)
    calculation = Calculator()
    calculation.show()
    qt.exec()
