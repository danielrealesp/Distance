import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Labels")
        self.setGeometry(50,50,300,300)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.move(120,50)
        self.passTextBox = QLineEdit(self)
        self.nameTextBox.move(120,80)
        self.passTextBox.move(120,110)
        self.nameTextBox.setPlaceholderText("Name...")
        self.passTextBox.setPlaceholderText("Password...") 
        self.passTextBox.setEchoMode(QLineEdit.Password)
        button = QPushButton("Save",self)
        button.move(155, 150)
        button.clicked.connect(self.getValues)

        self.show()

    def getValues(self):
        name = self.nameTextBox.text()
        passw = self.passTextBox.text()
        print(name, passw)
        self.setWindowTitle("Your name is: " + name)





def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
