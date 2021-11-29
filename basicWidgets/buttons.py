import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Labels")
        self.setGeometry(50,50,300,300)
        self.UI()

    def UI(self):
        self.text = QLabel("MyText", self)
        btn1 = QPushButton("Enter", self)
        btn2 = QPushButton("Exit", self)
        self.text.move(160,50)
        btn1.move(100,80)
        btn2.move(200,80)
        self.show()
        btn1.clicked.connect(self.enterFunc)
        btn2.clicked.connect(self.exitFunc)
    
    def enterFunc(self):
        self.text.setText("Enter") 
        self.text.resize(150,20)

    def exitFunc(self):
        self.text.setText("Exit") 
        self.text.resize(150,20)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
