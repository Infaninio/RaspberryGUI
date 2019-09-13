import PyQt5.QtMultimedia
import PyQt5.QtMultimediaWidgets

from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QPushButton
from os import listdir

MUSIKPATH = "E:"


class MediaPlayer():
    def __init__(self):
        #super().__init__()
        self.player = QMediaPlayer()
        self.currPlaylist = QMediaPlaylist(self.player)

        self.player.mediaStatusChanged.connect(self.newStatus)
        self.player.error.connect(self.playererror)
        self.playLists = {"default": "empty"}
        playliststmp = listdir(MUSIKPATH + "\\Playlists\\")

        for element in playliststmp:
            if ".m3u" in element:
                self.playLists[element[:-4]] = MUSIKPATH + "/Playlists/" + element





    def newStatus(self, status):
        print(self.player.mediaStatus())
        if status == QMediaPlayer.LoadedMedia:
            self.player.play()

    def playererror(self, error):
        print("Error: " + error)

    def getPlaylistNames(self):
        return self.playLists.keys()

    def setPlayList(self, playList):
        self.playLists["default"] = playList
        self.loadPlayList(self.playLists[playList])

    def loadPlayList(self, playlistPath):
        file = open(playlistPath, "r")
        self.currPlaylist.clear()
        for line in file:
            path = MUSIKPATH + line
            #Zeilenumbruch am ende des Pfad Stringes hat dazu geführt dass die Datei nicht gefunden werden konnnten, fällt das "\n" weg ist es kein Problem mehr
            path = path[:-1]
            self.currPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
            print(path)
        
            
            
            #self.player.setMedia(QMediaContent(self.currPlaylist))
        self.player.setPlaylist(self.currPlaylist)
        self.player.playlist().setCurrentIndex(1)
        #self.player.setMedia(QMediaContent(QUrl.fromLocalFile("\\Music\\5 Seconds Of Summer\\Unknown Album\\# - Youngblood.mp3")))


    def play(self):
        #self.player.play()
        print(self.player.mediaStatus())

    def pause(self):
        #self.player.pause()
        print("nothing")


    def numberOfPlaylists(self):
        return len(self.playLists) - 1