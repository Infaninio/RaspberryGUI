# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import src.IoController as ioContr

IMAGEPATH = "C:/Users/marti/source/repos/RaspberryGUI/img"


class Window():
    # State Machine für die Anzeige
    def __init__(self):
        self.mainWin = MainWindow(self)
        self.musikWin = MusikWinGen(self)
        self.mainWin.show()
        self.musikStat = False

    def changeToMusik(self, arg):
        self.musikWin.show()
        self.mainWin.hide()
    def changeToMenu(self, arg):
        self.mainWin.show()
        self.musikWin.hide()


    def playMusik(self, arg):
        if self.musikStat == True:
            self.musikStat = False
            print("Musik wiedergeben")
        else:
            self.musikStat = True
            print("Musik pausieren")

    def nextTitle(self, arg):
        print("Next Title")

    def prevTitle(self, arg):
        print("Last Title")


class GenWindow(QMainWindow):
    """description of class"""
   
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.setGeometry(0,0,800,480)
        self.setWindowTitle('RaspberryTouch')

        self.setObjectName("GenWindow")

        styleSheetStr = "QMainWindow#GenWindow{background-image: url(" + IMAGEPATH + "/rapibackresize.jpg" + ");}"
        self.setStyleSheet(styleSheetStr)

        self.setWindowFlag(Qt.FramelessWindowHint)

        #Leiste
        leiste = QWidget(self)
        leiste.setStyleSheet("background: transparent")
        leiste.setGeometry(0,420,800,60)

        closeBt = QPushButton("Ende", leiste)

        closeBt.clicked.connect(self.close)
        closeBt.setGeometry(0,0,200,60)
        closeBt.setFont(QFont("Calibri", 37, QFont.Bold))
        closeBt.setStyleSheet("QPushButton{background-image: url(" + IMAGEPATH + "/icobackleiste.png" + ");color: white;}")
        closeBt.setFlat(True)


        musikWd = QWidget(leiste)
        musikWd.setStyleSheet("background: transparent")
        musikWd.setGeometry(200,0,400,60)
        
        self.playM = QPushButton(musikWd)
        self.playM.setGeometry(140,0,120,60)
        self.playM.setFlat(True)
        self.playM.setIcon(QIcon(IMAGEPATH + "/icoplay.png"))
        self.playM.setIconSize(QSize(80,40))
        self.playM.clicked.connect(self.playBtCl)

        prevMBt = QPushButton(musikWd)
        prevMBt.setGeometry(20,0,120,60)
        prevMBt.setFlat(True)
        prevMBt.setIcon(QIcon(IMAGEPATH + "/icoprev.png"))
        prevMBt.setIconSize(QSize(80,40))
        prevMBt.clicked.connect(self.window.prevTitle)
        
      
        nextMBt = QPushButton(musikWd)
        nextMBt.setGeometry(260,0,120,60)
        nextMBt.setFlat(True)
        nextMBt.setIcon(QIcon(IMAGEPATH + "/iconext.png"))
        nextMBt.setIconSize(QSize(80,40))
        nextMBt.clicked.connect(self.window.nextTitle)



        menuBt = QPushButton("Menü", leiste)
        menuBt.setGeometry(600,0,200,60)
        menuBt.setFont(QFont("Calibri", 37, QFont.Bold))
        menuBt.setStyleSheet("QPushButton{background-image: url(" + IMAGEPATH + "/icobackleiste.png" + "); color: white;}")
        menuBt.clicked.connect(self.window.changeToMenu)
        menuBt.setFlat(True)


    def playBtCl(self, arg):
        self.window.playMusik(arg)
        if self.window.musikStat == True:
            self.playM.setIcon(QIcon(IMAGEPATH + "/icopause.png"))
        else:
            self.playM.setIcon(QIcon(IMAGEPATH + "/icoplay.png"))
        


    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Nachricht", "Soll die Anwendung geschlossen werden?", QMessageBox.Yes | QMessageBox.No)

        if(reply == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()



class MainWindow(GenWindow):

    def __init__(self, window):
        super().__init__(window)

        #String für den Button Hintergrund
        styleSheetStr = "QPushButton{background-image: url(" + IMAGEPATH + "/icoback2kl.png" + ");}"

        #Computer Button
        computerBt = QPushButton(self)
        computerBt.setGeometry(110,60,128,128)
        computerBt.setFlat(True)
        computerBt.setStyleSheet(styleSheetStr)
        computerBt.setIcon(QIcon(IMAGEPATH + "/computer.png"))
        computerBt.setIconSize(QSize(110,110))
        computerBt.clicked.connect(ioContr.bootPC)

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
        musikBt.clicked.connect(self.window.changeToMusik)

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


class MusikWinGen(GenWindow):
    def __init__(self, window):
        super().__init__(window)
        Button = QPushButton("Ein schöner Button",self)
        Button.setGeometry(100,100,100,100)




class AvWindow(GenWindow):
    def __init__(self, window):
        super().__init__(window)
