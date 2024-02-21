import os
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel
)

basedir = os.path.dirname(__file__)
imagesdir = 'C:/Users/AstroX/PycharmProjects/Create GUI Applications with Python & Qt6/Images/burger.jpg'
print("Current woring folder : ", os.getcwd())
print("Paths are relative to : ", basedir)
print("Images Folder : ", os.path.exists(imagesdir))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(imagesdir)))

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()