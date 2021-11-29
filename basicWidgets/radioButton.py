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
        self.name.move(150,50)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.move(150,80)
        self.surname.setPlaceholderText("Enter your surname")
        self.male = QRadioButton("Male", self)
        self.male.setChecked(True)
        self.female = QRadioButton("Female", self)
        self.female.move(200,110)
        self.male.move(150,110)
        btnSubmit = QPushButton("Submit", self) 
        btnSubmit.clicked.connect(self.submit)

        self.show()

    def submit(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print("Mr " + name + " " +  surname)        

        elif self.female.isChecked():
            print("Mrs " + name + " " +  surname)        


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
