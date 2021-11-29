import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider Widget")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()        
        self.slider = QSlider(Qt.Horizontal) 
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.txt1 = QLabel("0")
        self.txt1.setAlignment(Qt.AlignCenter)
        self.txt2 = QLabel("Hello World")
        vbox.addStretch()
        vbox.addWidget(self.txt2)
        vbox.addWidget(self.txt1)
        vbox.addWidget(self.slider)

        self.slider.valueChanged.connect(self.getValue)

        self.setLayout(vbox)
        self.show()

    def getValue(self):

        value = self.slider.value()
        font = QFont("Cambria", value)
        self.txt2.setFont(font)
        self.txt1.setText(str(value))



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()