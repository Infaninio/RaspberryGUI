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
        self.currPlaylist = QMediaPlaylist()

        self.player.mediaStatusChanged.connect(self.newStatus)




        self.playLists = {"default": "empty"}
        playliststmp = listdir(MUSIKPATH + "\\Playlists\\")

        for element in playliststmp:
            if ".m3u" in element:
                self.playLists[element[:-4]] = MUSIKPATH + "/Playlists/" + element





    def newStatus(self, status):
        print(status)
        if status == QMediaPlayer.LoadedMedia:
            print("loaded")
            self.player.play()

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
            path.replace("\\", "\\\\")
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            print(path)
        
        self.currPlaylist.setCurrentIndex(1)
        self.player.setPlaylist(self.currPlaylist)
        #self.player.setMedia(QMediaContent(QUrl.fromLocalFile("E:\Musik\Martin\(I Can't Get No) Satisfaction.mp3")))
        print(self.player.mediaStatus())

    def play(self):
        #self.player.play()
        print(self.player.mediaStatus())

    def pause(self):
        #self.player.pause()
        print("nothing")


    def numberOfPlaylists(self):
        return len(self.playLists) - 1