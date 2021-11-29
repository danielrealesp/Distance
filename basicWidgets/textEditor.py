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
        self.editor = QTextEdit(self)
        self.editor.move(150,80)
        button = QPushButton("Send", self)
        button.move(330,280)
        button.clicked.connect(self.getValue)

        self.show()
    
    def getValue(self):
        #We need to use plainText because the TextEdit widget accepts rich text 
        text = self.editor.toPlainText()
        print(text)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
