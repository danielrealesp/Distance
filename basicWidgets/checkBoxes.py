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
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter name...")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter surname...")
        self.remember = QCheckBox("Remember me", self)
        self.name.move(100,50)
        self.surname.move(100,80)
        self.remember.move(120,110)
        btnSubmit = QPushButton("Submit",self)
        btnSubmit.move(200,140)
        btnSubmit.clicked.connect(self.submit)
        self.show()

    def submit(self):
        if (self.remember.isChecked()):
            print("Remember: " + self.name.text() +  "\n" + self.surname.text())
            pass
        else:
            print("Not remember")


        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
