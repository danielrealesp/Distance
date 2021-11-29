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
        self.combo = QComboBox(self)
        self.combo.move(150,100)
        button = QPushButton("Save", self)
        button.clicked.connect(self.submit)
        button.move(150,130)

        self.combo.addItem("Python")
        self.setStyleSheet("""
            background: blue;
        """)
        self.combo.addItems(["C", "Clojure", "Java"])
        
        self.show()

    def submit(self):
        selected = self.combo.currentText()
        print(selected)


        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
