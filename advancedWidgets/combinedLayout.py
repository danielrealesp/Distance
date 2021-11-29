import sys
from PyQt5.QtWidgets import * 


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        leftLayout = QVBoxLayout()
        leftLayout.setContentsMargins(10,50,10,0)
        rightLayout = QHBoxLayout()
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        botones = []
        btn1 = QPushButton("Iniciar")
        botones.append(btn1)
        btn2 = QPushButton("Terminar")
        botones.append(btn2)
        btn3 = QPushButton("Registros")
        botones.append(btn3)

        for boton in botones:
            leftLayout.addWidget(boton)

        leftLayout.addStretch()

        rightLayout.addStretch()
        botones2 = []
        btn4 = QPushButton("Calibrar")
        botones2.append(btn4)
        btn5 = QPushButton("Duración")
        botones2.append(btn5)
        btn6 = QPushButton("Salir")
        botones2.append(btn6)
        
        for boton in botones2:
            rightLayout.addWidget(boton)

        rightLayout.addStretch()

        self.setLayout(mainLayout)

        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()