from os import listdir, path
import pygame
import random
import platform

MUSIKPATH = "E:"


class MediaPlayer():
    def __init__(self):

        print(platform.platform())

        if "Win" in platform.platform():
            MUSIKPATH = "E:"
        else:
            MUSIKPATH = "/home/pi/Music/sync"

        pygame.init()
        pygame.mixer.init()
        pygame.mixer_music.set_endevent(pygame.USEREVENT)
        pygame.mixer_music.set_volume(50)
        self.playList = list()
        self.plPos = 0
        self.state = False
        self.chgSrc = False


        self.playLists = dict()
        playliststmp = listdir(MUSIKPATH + path.sep + "Playlists" + path.sep)

        for element in playliststmp:
            if ".m3u" in element:
                self.playLists[element[:-4]] = MUSIKPATH + path.sep + "Playlists" + path.sep + element


    def getPlaylistNames(self):
        return self.playLists.keys()

    def setPlayList(self, playList):
        self.loadPlayList(self.playLists[playList])

    def loadPlayList(self, playlistPath):
        file = open(playlistPath, "r")
        self.playList.clear()
        for line in file:
            flpath = MUSIKPATH + line
            flpath = flpath.replace("/", path.sep)
            flpath = flpath.replace("\\",path.sep)
            #Zeilenumbruch am ende des Pfad Stringes hat dazu geführt dass die Datei nicht gefunden werden konnnten, fällt das "\n" weg ist es kein Problem mehr
            flpath = flpath[:-1]
            self.playList.append(flpath)
            print(flpath)

        self.plPos = 0
        random.shuffle(self.playList)
        pygame.mixer_music.load(self.playList[self.plPos])
        pygame.mixer_music.play()
        self.state = True


    def playPause(self, arg=0):
        if self.state:
            #Player is running, need to pause
            pygame.mixer_music.pause()
            self.state = False
            return False
        else:
            pygame.mixer_music.unpause()
            self.state = True
            return True

    def next(self,arg=0):
        pygame.mixer_music.stop()
        self.changePos(1)
        pygame.mixer_music.load(self.playList[self.plPos])
        pygame.mixer_music.play()
        self.state = True
        self.chgSrc = True

    def prev(self,arg=0):
        pygame.mixer_music.stop()
        self.changePos(-1)
        pygame.mixer_music.load(self.playList[self.plPos])
        pygame.mixer_music.play()
        self.state = True
        self.chgSrc = True

    def changePos(self, diff):
        self.plPos += diff
        if self.plPos < 0:
            random.shuffle(self.playList)
            self.plPos = 0
        elif self.plPos > len(self.playList):
            random.shuffle(self.playList)
            self.plPos = 0


    def numberOfPlaylists(self):
        return len(self.playLists) - 1


    def playing(self):
        return self.state


    def eventLoop(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.USEREVENT:
                if self.chgSrc == True:
                    self.chgSrc = False
                else:
                    #Song zu Ende
                    self.changePos(1)
                    pygame.mixer_music.load(self.playList[self.plPos])
                    pygame.mixer_music.play()
