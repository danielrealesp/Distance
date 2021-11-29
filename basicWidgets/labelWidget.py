import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Labels")
        self.setGeometry(50,50,300,300)
        self.UI()

    def UI(self):
        # Hay que decirle donde desplegarlo
        lbl1 = QLabel("Hello Python", self)
        lbl2 = QLabel("Hello World", self)
        lbl1.move(100,50)
        lbl2.move(150,100)

        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
