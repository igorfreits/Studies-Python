"""Integrando janelas do QT Designer com PyQT5

-Para converter um .ui para .py
    escrever no terminal: pyuic5 'nome do arquivo.ui' -o 'novo nome.py'

"""
import sys
from designer import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class New(QMainWindow, Ui_MainWindow):  # Importa class criada no QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnChooseFile.clicked.connect(
            self.open_image)  # Botão para abrir as imagens
        self.btnResize.clicked.connect(self.resize_image)
        self.btnSave.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open image',
            r'C:\Users\Igor\Desktop\Estudos\Programação-em-Python'
            r'\Mundo-invertido\Udemy\4-Módulos-Python\image'
        )
        self.inputOpenFile.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        # exibi largura e Altura da imagem selecionada
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def resize_image(self):
        # Cria uma nova imagem e a redimensiona pela ALTURA
        width = int(self.inputWidth.text())
        self.new_image = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_image)

        self.inputWidth.setText(str(self.new_image.width()))
        self.inputHeight.setText(str(self.new_image.height()))

    def save(self):
        # Salva o arquivo
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'save image',
            r'C:\Users\Igor\Desktop'
        )
        self.new_image.save(image, 'PNG')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    new = New()
    new.show()
    qt.exec()
