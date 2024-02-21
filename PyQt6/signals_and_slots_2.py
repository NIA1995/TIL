from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me !")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You Already clicked me !")
        self.button.setEnabled(False)

        self.setWindowTitle("My OneShot App")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()