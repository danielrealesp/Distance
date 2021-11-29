import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer


font = QFont("Cambria", pointSize=20)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.setGeometry(50,50,300,300)
        self.UI()

    def UI(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250,250)
        self.colorLabel.setStyleSheet("""
            background-color:green;
        """)

        self.colorLabel.move(40,20)

        ######## Botones
        btnStart = QPushButton("Start", self)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.clicked.connect(self.stop)
        btnStart.move(80,300)
        btnStop.move(190,300)

        ####### Timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0

        self.show()

    def changeColor(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet("""
            background-color:red;
            """)

            self.value = 1

        elif self.value == 1:
            self.colorLabel.setStyleSheet("""
            background-color:blue;
            """)
            self.value = 2

        elif self.value == 2:
            self.colorLabel.setStyleSheet("""
            background-color:green;
            """)

            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
