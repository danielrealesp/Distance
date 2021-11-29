import sys
from PyQt5.QtWidgets import * 


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        btn1 = QPushButton("Boton 1")
        btn2 = QPushButton("Boton 2")
        btn3 = QPushButton("Boton 3")
        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addStretch()
        self.setLayout(vbox)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()