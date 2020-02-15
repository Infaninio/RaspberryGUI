import yaml
import time
import os

YamlPath = "config.yml"

class YamlReader:
    def __init__(self,path = YamlPath):
        #Nichts machen, gibt kein Init da kein konkretes Objekt entstehen soll/wird 
        return 0



    def setPath(path):
        YamlPath = path



    # funktionen wenn kein Klassen Objekt erstellt wird. Die Datei wird jedesmal neu geladen
    def add(Key, Value):
        stream = open(YamlPath, "r")
        data = yaml.load(stream, yaml.SafeLoader)
        stream.close()

        stream = open(YamlPath, "w")
        if data == None:
            #Sonder Behandlung da sonst data leer ist und python nicht weiss dass das ein Dict werden soll
            data = {"Last Modified": time.strftime("%d.%m.%Y")}
        data[Key] = Value
        data["Last Modified"] = time.strftime("%d.%m.%Y")
        yaml.dump(data, stream)
        stream.close()




    def get(Key):
        stream = open(YamlPath, "r")
        data = yaml.load(stream, yaml.SafeLoader)
        stream.close()
        if data == None:
            return "File is empty"
        return data[Key]
    pass

