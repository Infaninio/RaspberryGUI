import PyQt5.QtMultimedia
import PyQt5.QtMultimediaWidgets

from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PyQt5.QtCore import QUrl
from os import listdir

MUSIKPATH = "Z:"


class MediaPlayer:
    def __init__(self):
        self.player = QMediaPlayer()
        self.currPlaylist = QMediaPlaylist()

        self.playLists = {"default": "empty"}

        playliststmp = listdir(MUSIKPATH + "/Playlists")

        for element in playliststmp:
            if ".m3u" in element:
                self.playLists[element[:-4]] = MUSIKPATH + "/Playlists/" + element




    def getPlaylistNames(self):
        return self.playLists.keys()

    def setPlayList(self, playList):
        print("Playlist " + playList + " wird abgespielt")
        self.playLists["default"] = playList
        self.loadPlayList(self.playLists[playList])

    def loadPlayList(self, playlistPath):
        print("Playlist setzten")

    def play(self):
        print("Play")

    def numberOfPlaylists(self):
        return len(self.playLists) - 1