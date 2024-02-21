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

        button = QPushButton("Press Me !")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    # 어떻게 checked 인자가 값이 변하는가?
    # PyQt6에서는 신호가 방출될 때 신호와 함께 추가 정보를 전달할 수 있습니다. 'QPushButton'의 '클릭' 신호는 버튼이 현재 선택되어 있는지 여부를 나타내는 'bool' 값을 내보냅니다.
    #
    # 제공된 코드에서 clicked 신호는 checked 매개변수를 허용하는 the_button_was_toggled 메소드에 연결됩니다. 이 매개변수는 clicked 신호를 내보낼 때 PyQt6에서 자동으로 제공되며 버튼의 현재 상태(선택 또는 선택 취소)를 나타냅니다.
    #
    # 따라서 checked 매개변수를 명시적으로 할당하지 않았더라도 PyQt6은 이를 뒤에서 처리하고 신호가 방출될 때 버튼의 상태에 따라 적절한 값을 제공합니다.
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

