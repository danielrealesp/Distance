import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


font = QFont("Cambria", pointSize=20)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.setGeometry(50,50,300,300)
        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150,100)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(25)
        self.spinBox.setMaximum(200)
        self.spinBox.setSuffix("$ ")
        self.spinBox.setPrefix(" cm")
        self.spinBox.setSingleStep(10)
        self.spinBox.valueChanged.connect(self.getValue)

        self.show()

    def getValue(self):
        value = self.spinBox.value()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
