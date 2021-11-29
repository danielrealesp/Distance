import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):

        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("Get")
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.table.setRowCount(5)
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("Last Name"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("Address"))
#
#        self.table.horizontalHeader().hide()
#        self.table.verticalHeader().hide()
#
        self.table.setItem(0,0, QTableWidgetItem("First Item"))

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        btn.clicked.connect(self.getValue)

        self.table.doubleClicked.connect(self.getValue)
        self.setLayout(vbox)

        self.show()

    def getValue(self):
        
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()