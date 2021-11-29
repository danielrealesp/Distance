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
        btn = QPushButton("Click me", self)
        btn1 = QPushButton("Information", self)
        btn1.clicked.connect(self.information)
        btn.setFont(font)
        btn.move(200,150)
        btn.clicked.connect(self.clicked)
        self.show()

    def clicked(self):
        mbox = QMessageBox.question(self, "Warning!","Are you sure you want to exit?", QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if mbox == QMessageBox.Yes:
            sys.exit()
        elif mbox == QMessageBox.No:
            print("Click no")

    def information(self):
        mbox = QMessageBox.information(self, "Information", "You logged out")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
