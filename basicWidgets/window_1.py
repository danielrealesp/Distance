import sys
from PyQt5.QtWidgets import * 
from principal import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        # Primeros dos parámetros son donde comienza la ventana y ultimos dos el tamaño
        self.setGeometry(50,50, 300, 450)
        self.setWindowTitle("Ventana de Prueba")

App = QApplication(sys.argv)

window = Window()
ui_MainWindow = Ui_MainWindow()
ui_MainWindow.setupUi(window)
window.show()

sys.exit(App.exec_())





