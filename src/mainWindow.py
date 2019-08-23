from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    """description of class"""
   
   
    def __init__(self):
        super().__init__()



        self.setGeometry(0,0,800,480)
        self.setWindowTitle('RaspberryTouch')

        self.setObjectName("MainWindow")
        self.setStyleSheet("QMainWindow#MainWindow{background-image: url(C://sync/rapibackresize.jpg);}")


        #Leiste
        leiste = QWidget(self)
        leiste.setStyleSheet("background: transparent")
        leiste.setGeometry(0,420,800,60)

        closeBt = QPushButton("EXIT", leiste)
        closeBt.setGeometry(0,0,200,60)
        closeBt.setFont(QFont("Calibri", 37, QFont.Bold))

        dateLb = QLabel("Das ist Ein Text",leiste)
        dateLb.setGeometry(200,0,400,60)
        dateLb.setAlignment(Qt.AlignCenter)
        dateLb.setFont(QFont("Calibri", 30, QFont.Bold))
        

        menuBt = QPushButton("Menü", leiste)
        menuBt.setGeometry(600,0,200,60)
        menuBt.setFont(QFont("Calibri", 37, QFont.Bold))




    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Nachricht", "Soll die Anwendung geschlossen werden?", QMessageBox.Yes | QMessageBox.No)

        if(reply == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()



