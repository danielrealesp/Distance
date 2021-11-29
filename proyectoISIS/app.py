import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from ventana_principal import * 

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())