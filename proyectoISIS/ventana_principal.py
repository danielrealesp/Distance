# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ventana1ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

from prototipo import Distance

count = 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        MainWindow.setStyleSheet("  background: url(./imagenes/background.jpg);\n"
"  background-repeat: no-repeat;\n"
"  background-size: 100% 100%;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layoutPrincipal = QtWidgets.QVBoxLayout()
        self.layoutPrincipal.setObjectName("layoutPrincipal")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutPrincipal.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutPrincipal.addWidget(self.label)
        self.layoutBotones = QtWidgets.QHBoxLayout()
        self.layoutBotones.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layoutBotones.setObjectName("layoutBotones")
        self.btnCalibrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalibrar.clicked.connect(self.iniciarCalibracion)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btnCalibrar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnCalibrar.setFont(font)
        self.btnCalibrar.setObjectName("btnCalibrar")
        self.layoutBotones.addWidget(self.btnCalibrar)
        self.btnIniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIniciar.clicked.connect(self.iniciar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btnIniciar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setObjectName("btnIniciar")
        self.layoutBotones.addWidget(self.btnIniciar)
        self.btnTerminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnTerminar.clicked.connect(self.terminar)  
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btnTerminar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnTerminar.setFont(font)
        self.btnTerminar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnTerminar.setObjectName("btnTerminar")
        self.layoutBotones.addWidget(self.btnTerminar)
        self.layoutPrincipal.addLayout(self.layoutBotones)
        self.layoutSlider = QtWidgets.QHBoxLayout()
        self.layoutSlider.setObjectName("layoutSlider")
        self.lblInfoDistancia = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblInfoDistancia.setFont(font)
        self.lblInfoDistancia.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblInfoDistancia.setObjectName("lblInfoDistancia")
        self.layoutSlider.addWidget(self.lblInfoDistancia)
        self.sliderDistancia = QtWidgets.QSlider(self.centralwidget)
        self.sliderDistancia.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDistancia.setObjectName("sliderDistancia")
        self.sliderDistancia.setMinimum(30)
        self.sliderDistancia.setMaximum(300)
        self.sliderDistancia.setTickInterval(10)
        self.sliderDistancia.valueChanged.connect(self.getValue)
        self.layoutSlider.addWidget(self.sliderDistancia)
        self.lblDistancia = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblDistancia.setFont(font)
        self.lblDistancia.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblDistancia.setObjectName("lblDistancia")
        self.layoutSlider.addWidget(self.lblDistancia)
        self.layoutPrincipal.addLayout(self.layoutSlider)
        self.btnRegistros = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnRegistros.setFont(font)
        self.btnRegistros.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnRegistros.setObjectName("btnRegistros")
        self.layoutPrincipal.addWidget(self.btnRegistros)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutPrincipal.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.layoutPrincipal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.progressBar = QtWidgets.QProgressBar()
        self.layoutPrincipal.addWidget(self.progressBar)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.runProgressBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Distance"))
        self.label.setText(_translate("MainWindow", "Distance"))
        self.btnCalibrar.setText(_translate("MainWindow", "CALIBRAR"))
        self.btnIniciar.setText(_translate("MainWindow", "INICIAR"))
        self.btnTerminar.setText(_translate("MainWindow", "TERMINAR"))
        self.lblInfoDistancia.setText(_translate("MainWindow", "Distancia (en cm) : "))
        self.lblDistancia.setText(_translate("MainWindow", "0"))
        self.btnRegistros.setText(_translate("MainWindow", "REGISTROS"))
    
    def runProgressBar(self):
        print("Calibrar clicked")
        global count
        count +=1
        self.progressBar.setValue(count)
        if count == 100:
            self.timer.stop()
            mbox = QtWidgets.QMessageBox.information(self.main, "Calibración Terminada", "La calibración terminó exitosamente")

    def iniciarCalibracion(self):
        self.timer.start()

    def iniciar(self):
        print("Iniciar Clicked")
        distanciaStr = self.lblDistancia.text()
        distancia = int(distanciaStr)
        path1 = os.path.abspath("imagen1.jpg")
        calculador = Distance()
        focal = calculador.calibrarFocal(path1)
        calculador.app(focal,distancia)



    def terminar(self):
        print("Terminar clicked")
    
    def getValue(self):
        value = self.sliderDistancia.value()
        self.lblDistancia.setText(str(value))

