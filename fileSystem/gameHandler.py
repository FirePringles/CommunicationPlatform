from gameUtil import GameUtil

class GameHandler:
        
    def saveGameState(gameDict):
        """
            Saves a game state into a json file called gameState
            Arguments:
                self: the current GameHandler
                gameDict: An dictionary containing the status of a game
        """
        gameUtil = GameUtil()
        try:
            if(GameHandler.validateDict(gameDict)):
                gameUtil.write(gameDict)
                return  0
            else:
                print("Dictionary is not in the correct format")
                return 2
        except Exception as e:
            print("Failed to save game state: " + str(e))
            return 1

    def loadGameState():
        """
            Reads and returns the current status of the gameState json file.
            Arguments:
                self: the current GameHandler
        """
        gameUtil = GameUtil()
        try:
            data = gameUtil.read()
            if GameHandler.validateDict(data):
                return data
            else: 
                print("Loaded game is not in the correct format. It might be corrupted")
                return 2
        except Exception as e:
            print("Failed to load game state: " + str(e))
            return 1

    def changeFilePath(path):
        """
            Sets a new path where the data of the game will be loaded and saved from/to
            Arguments:
                path: a string containing the new path to read and save from
            Example:
                changeFilePath("newGameState.json") -> sets new path to file called newGameState.json
        """
        return GameUtil.changeFilePath(path)


    def validateDict(gameDict):
        """
            Validates that a dictionary has the correct structure for a game 
            Arguments:
                gameDict: An dictionary containing the status of a game
        """

        if type(gameDict) is dict:
            game = gameDict["game"]
        else:
            return False

        length = abs(len(game["listofPiecesPlayer1"]) - len(game["listofPiecesPlayer2"]))
        if length >= 1:
            return False
        if (game["boardSize"] > 24 or game["boardSize"] < 6):
            return False
        if (game["player1"]["color"] != "black" and game["player1"]["color"] != "white"):
            return False
        if (game["player2"]["color"] != "black" and game["player2"]["color"] != "white"):
            return False
        if (game["player1"]["isNext"] == game["player2"]["isNext"]):
            return False
        if (game["player1"]["color"] == game["player2"]["color"]):
            return False

        if game["player1"]["isNext"]:
            if game["player1"]["nextMove"]["x"] > game["boardSize"] or game["player1"]["nextMove"]["x"] < 0:
                return False
            if game["player1"]["nextMove"]["y"] > game["boardSize"] or game["player1"]["nextMove"]["y"] < 0:
                return False
            if game["player1"]["nextMove"]["x"] == 0 or game["player1"]["nextMove"]["y"] == 0:
                if game["player1"]["nextMove"]["x"] != game["player1"]["nextMove"]["y"]:
                    return False
        else: 
            if game["player1"]["nextMove"]["x"] > 0 or game["player1"]["nextMove"]["y"] > 0:
                return False

        if game["player2"]["isNext"]:
            if game["player2"]["nextMove"]["x"] > game["boardSize"] or game["player2"]["nextMove"]["x"] < 0:
                return False
            if game["player2"]["nextMove"]["y"] > game["boardSize"] or game["player2"]["nextMove"]["y"] < 0:
                return False
            if game["player2"]["nextMove"]["x"] == 0 or game["player2"]["nextMove"]["y"] == 0:
                if game["player2"]["nextMove"]["x"] != game["player2"]["nextMove"]["y"]:
                    return False
        else: 
            if game["player2"]["nextMove"]["x"] > 0 or game["player2"]["nextMove"]["y"] > 0:
                return False

        for piece in game["listofPiecesPlayer1"]:
            if piece["location"]["x"] < 0 or piece["location"]["x"] > game["boardSize"]:
                return False
            if piece["location"]["y"] < 0 or piece["location"]["y"] > game["boardSize"]:
                return False
            if len(piece["properties"]) > 10:
                return False

        for piece in game["listofPiecesPlayer2"]:
            if piece["location"]["x"] < 0 or piece["location"]["x"] > game["boardSize"]:
                return False
            if piece["location"]["y"] < 0 or piece["location"]["y"] > game["boardSize"]:
                return False
            if len(piece["properties"]) > 10:
                return False
        return True




    def testSaveGameState(gameDict):
        """
            Test function that writes the information from a dictionary into a json file called testData
            Arguments:
                gameDict: An dictionary containing the status of a test game
        """
        try:
            if(GameHandler.validateDict(gameDict)):
                if GameUtil.testWrite(gameDict) != 1:
                    return  0
            else:
                return 1
        except:
            return 2

    
    def testLoadGameState(path):
        """
            Test function that reads and returns the content of a json file.
            Arguments:
                path: The filename of the file one wants to read
        """
        try:
            return GameUtil.testRead(path)
        except:
            return 1

