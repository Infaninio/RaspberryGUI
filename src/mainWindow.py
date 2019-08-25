# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

IMAGEPATH = "C:/Users/marti/source/repos/RaspberryGUI/img"

class GenWindow(QMainWindow):
    """description of class"""
   
   
    def __init__(self):
        super().__init__()



        self.setGeometry(0,0,800,480)
        self.setWindowTitle('RaspberryTouch')

        self.setObjectName("GenWindow")

        styleSheetStr = "QMainWindow#GenWindow{background-image: url(" + IMAGEPATH + "/rapibackresize.jpg" + ");}"
        self.setStyleSheet(styleSheetStr)


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



class MainWindow(GenWindow):

    def __init__(self):
        super().__init__()

        #String für den Button Hintergrund
        styleSheetStr = "QPushButton{background-image: url(" + IMAGEPATH + "/icoback2kl.png" + ");}"

        #Computer Button
        computerBt = QPushButton(self)
        computerBt.setGeometry(110,60,128,128)
        computerBt.setFlat(True)
        computerBt.setStyleSheet(styleSheetStr)
        computerBt.setIcon(QIcon(IMAGEPATH + "/computer.png"))
        computerBt.setIconSize(QSize(110,110))

        #CD Button
        cdBt = QPushButton(self)
        cdBt.setGeometry(336,60,128,128)
        cdBt.setFlat(True)
        cdBt.setStyleSheet(styleSheetStr)
        cdBt.setIcon(QIcon(IMAGEPATH + "/cd.png"))
        cdBt.setIconSize(QSize(110,110))

        #Radio Button
        musikBt = QPushButton(self)
        musikBt.setGeometry(562,60,128,128)
        musikBt.setFlat(True)
        musikBt.setStyleSheet(styleSheetStr)
        musikBt.setIcon(QIcon(IMAGEPATH + "/musik.png"))
        musikBt.setIconSize(QSize(110,110))

        avBt = QPushButton(self)
        avBt.setGeometry(110,232,128,128)
        avBt.setFlat(True)
        avBt.setStyleSheet(styleSheetStr)
        avBt.setIcon(QIcon(IMAGEPATH + "/av.png"))
        avBt.setIconSize(QSize(110,110))

        beamerBt = QPushButton(self)
        beamerBt.setGeometry(336,232,128,128)
        beamerBt.setFlat(True)
        beamerBt.setStyleSheet(styleSheetStr)
        beamerBt.setIcon(QIcon(IMAGEPATH + "/beamer.png"))
        beamerBt.setIconSize(QSize(110,110))

        einstellungenBt = QPushButton(self)
        einstellungenBt.setGeometry(562,232,128,128)
        einstellungenBt.setFlat(True)
        einstellungenBt.setStyleSheet(styleSheetStr)
        einstellungenBt.setIcon(QIcon(IMAGEPATH + "/einstellungen.png"))
        einstellungenBt.setIconSize(QSize(110,110))


