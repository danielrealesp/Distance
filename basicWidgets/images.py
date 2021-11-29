import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Labels")
        self.setGeometry(50,50,300,300)
        self.UI()

    def UI(self):
        #Only the self parameter
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/imagen1.png'))
        self.image.move(150,50)
        btnRemove = QPushButton("Remove",self)
        btnRemove.move(150,220)
        btnShow = QPushButton("Show", self)
        btnShow.move(150,250)
        btnShow.clicked.connect(self.showImage)
        btnRemove.clicked.connect(self.removeImage)
        self.show()
        self.show()

    def showImage(self):
        self.image.show()

    def removeImage(self):
        self.image.close()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
