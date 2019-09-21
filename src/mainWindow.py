# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import src.IoController as ioContr
from src.mediaPlayer import MediaPlayer
import os
import platform

IMAGEPATH = "C:/Users/marti/source/repos/RaspberryGUI/img"



class Window():
    # State Machine für die Anzeige
    def __init__(self):
        if "win" in platform.platform():
            IMAGEPATH = "C:/Users/marti/source/repos/RaspberryGUI/img"
        else:
            IMAGEPATH = "/home/pi/Desktop/RaspberryGUI/img"
        self.mediaPlayer = MediaPlayer()
        self.mainWin = MainWindow(self)
        self.musikWin = MusikWinGen(self)
        self.avWin = AvWindow(self)
        self.mainWin.show()

    def changeToMusik(self, arg):
        self.musikWin.show()
        self.mainWin.hide()
    def changeToMenu(self, arg):
        self.mainWin.show()
        self.musikWin.hide()
        self.avWin.hide()
    def changeToAv(self, arg):
        self.avWin.show()
        self.mainWin.hide()


class GenWindow(QMainWindow):
    """description of class"""
   
    def __init__(self, window):
        super().__init__()
        self.stateM = window
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
        closeBt.setFont(QFont("Calibri", 35, QFont.Bold))
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
        prevMBt.clicked.connect(self.stateM.mediaPlayer.prev)
        
      
        nextMBt = QPushButton(musikWd)
        nextMBt.setGeometry(260,0,120,60)
        nextMBt.setFlat(True)
        nextMBt.setIcon(QIcon(IMAGEPATH + "/iconext.png"))
        nextMBt.setIconSize(QSize(80,40))
        nextMBt.clicked.connect(self.stateM.mediaPlayer.next)



        menuBt = QPushButton("Menü", leiste)
        menuBt.setGeometry(600,0,200,60)
        menuBt.setFont(QFont("Calibri", 37, QFont.Bold))
        menuBt.setStyleSheet("QPushButton{background-image: url(" + IMAGEPATH + "/icobackleiste.png" + "); color: white;}")
        menuBt.clicked.connect(self.stateM.changeToMenu)
        menuBt.setFlat(True)


    def playBtCl(self, arg):
        if self.stateM.mediaPlayer.playPause():
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
        musikBt.clicked.connect(self.stateM.changeToMusik)

        #AV Button
        avBt = QPushButton(self)
        avBt.setGeometry(110,232,128,128)
        avBt.setFlat(True)
        avBt.setStyleSheet(styleSheetStr)
        avBt.setIcon(QIcon(IMAGEPATH + "/av.png"))
        avBt.setIconSize(QSize(110,110))
        avBt.clicked.connect(self.stateM.changeToAv)

        #Beamer Button
        beamerBt = QPushButton(self)
        beamerBt.setGeometry(336,232,128,128)
        beamerBt.setFlat(True)
        beamerBt.setStyleSheet(styleSheetStr)
        beamerBt.setIcon(QIcon(IMAGEPATH + "/beamer.png"))
        beamerBt.setIconSize(QSize(110,110))
        beamerBt.clicked.connect(ioContr.beamerPwr)

        einstellungenBt = QPushButton(self)
        einstellungenBt.setGeometry(562,232,128,128)
        einstellungenBt.setFlat(True)
        einstellungenBt.setStyleSheet(styleSheetStr)
        einstellungenBt.setIcon(QIcon(IMAGEPATH + "/einstellungen.png"))
        einstellungenBt.setIconSize(QSize(110,110))


class MusikWinGen(GenWindow):
    def __init__(self, window):
        super().__init__(window)

        styleSheetStr = "QPushButton{background-image: url(" + IMAGEPATH + "/icoback2PlayList.png" + "); color: white;}"
        PlListWg = QWidget(self)
        scrollLength = 70 * self.stateM.mediaPlayer.numberOfPlaylists()
        PlListWg.setGeometry(200,30,400,scrollLength)
        PlListWg.setStyleSheet("background-color: transparent")

        PlListSa = QScrollArea(self)
        PlListSa.setGeometry(200,30,450,350)
        PlListSa.setWidget(PlListWg)
        PlListSa.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        PlListSa.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        PlListSa.setStyleSheet("background-color:transparent;")
        PlListSa.setFrameStyle(QFrame.NoFrame)



        self.btList = QButtonGroup(self)
        self.btList.setExclusive(True)
        i = 0
        for element in self.stateM.mediaPlayer.getPlaylistNames():

            if element != "default":
                self.btList.addButton(QPushButton(element, PlListWg),i)
                self.btList.button(i).setGeometry(0,(i*60 )+ (i*10),400,60)
                self.btList.button(i).setFlat(True)
                self.btList.button(i).setStyleSheet(styleSheetStr)
                self.btList.button(i).setFont(QFont("Calibri", 25, QFont.Bold))
                i +=1

        self.btList.buttonClicked.connect(self.testprint) 


    def testprint(self, id):
        self.stateM.mediaPlayer.setPlayList(id.text())
        #print("Button Click"+ id.text())




class AvWindow(GenWindow):
    def __init__(self, window):
        super().__init__(window)


         #String für den Button Hintergrund
        styleSheetStr = "QPushButton{background-image: url(" + IMAGEPATH + "/icoback2kl.png" + ");}"

        pcAudioBt = QPushButton(self)
        pcAudioBt.setGeometry(110,143,128,128)
        pcAudioBt.setFlat(True)
        pcAudioBt.setStyleSheet(styleSheetStr)
        pcAudioBt.setIcon(QIcon(IMAGEPATH + "/computer.png"))
        pcAudioBt.setIconSize(QSize(110,110))
        pcAudioBt.clicked.connect(self.pcAudioCon)

        rpiAudioBt = QPushButton(self)
        rpiAudioBt.setGeometry(336,143,128,128)
        rpiAudioBt.setFlat(True)
        rpiAudioBt.setStyleSheet(styleSheetStr)
        rpiAudioBt.setIcon(QIcon(IMAGEPATH + "/raspberry.png"))
        rpiAudioBt.setIconSize(QSize(110,110))
        rpiAudioBt.clicked.connect(self.rpiAudioCon)

        bluerayAudioBt = QPushButton(self)
        bluerayAudioBt.setGeometry(562,143,128,128)
        bluerayAudioBt.setFlat(True)
        bluerayAudioBt.setStyleSheet(styleSheetStr)
        bluerayAudioBt.setIcon(QIcon(IMAGEPATH + "/blueray.png"))
        bluerayAudioBt.setIconSize(QSize(110,110))
        bluerayAudioBt.clicked.connect(self.bluerayAudioCon)






    def pcAudioCon(self, arg):
        ioContr.avPc()
        print("GAME Channel @Denon")

    def rpiAudioCon(self, arg):
        print("Connect Bluetooth @Denon")
        try:
            os.system("sudo echo -e \"connect 08:EF:3B:35:DE:2C\" | bluetoothctl > /dev/null 2>&1")
        except:
            print("Maybe not Raspbian")

    def bluerayAudioCon(self, arg):
        ioContr.avBlp()
        print("BlueRay Channel @Denon")