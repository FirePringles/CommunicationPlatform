import json
from configparser import ConfigParser

class GameUtil:

    def __init__(self):
        self.config = ConfigParser()

    """
        Writes the input argument to a json file specified by its path in the config file
        Arguments:
            self: the current GameHandler
            gameDict: An dictionary containing the status of a game
    """
    def write(self, gameDict):
        self.config.read("config.ini")
        path = self.config["DEFAULT"]["path"]
        try:
            with open(path, "w") as outfile:
                json.dump(gameDict, outfile)
        except:
            return 1


    """
        Reads and returns the data contained in the game documents file. 
        Arguments:
            self: the current GameHandler
    """
    def read(self):
        self.config.read("config.ini")
        path = self.config["DEFAULT"]["path"]
        try:
            with open(path) as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print("Error: Wrong File path or there exists no file to load")
            return 1
        except:
            return 1

    """
        Changes what document the gameUtil will read and write from 
        Arguments:
            path: the path to the new file one wants to use for game documentation
    """
    def changeFilePath(path):
        config = ConfigParser()
        config["DEFAULT"] = {"path":path}   
        with open("config.ini","w") as f:
            config.write(f)
        return

    def testRead(path):
        try:
            with open(path) as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print("Error: Wrong File path or there exists no file to load")
            return 1
        except:
            return 1


    def testWrite(gameDict):
        try:
            with open("testData.json", "w") as outfile:
                json.dump(gameDict, outfile)
        except:
            return 1