"""Instalação e primeiro contato com PyQT5

PyQt é uma toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicação GUI (Interface gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads,  comunicação de rede,
etc...

-https://doc.qt.io/qtforpython/
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # Cria um botão e insere um texto
        self.btn = QPushButton('Text Button')
        # Tamanho da fonte do botão
        self.btn.setStyleSheet("font-size:40px")
        # localização do botão
        # Linha, coluna/quantas linhas e colunas ira ocupar
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # Acaçoa clicar chamando um function
        self.btn.clicked.connect(self.action)

        # Ação ao clicar usando lambda
        # self.btn.clicked.connect(lambda: print('Hello World!'))
        # Manda o comando no terminal

        self.setCentralWidget(self.cw)

    def action(self):
        print('Good Morning')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()
