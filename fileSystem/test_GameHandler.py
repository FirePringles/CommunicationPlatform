from gameHandler import GameHandler
from configparser import ConfigParser

testString = "hello"
testDictGood1 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 7, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictGood2 = {"game": {"boardSize": 20, "player1": {"name": "Joachim", "color": "white", "isNext": True, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Vlad", "color": "black", "isNext": False, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3"], "order": 1},{"location": {"x": 4, "y": 19}, "properties": ["value1", "value2", "value3"], "order": 1},{"location": {"x": 1, "y": 2}, "properties": ["value1", "value2", "value3"], "order": 3},{"location": {"x": 5, "y": 5}, "properties": ["value1", "value2", "value3"], "order": 3},{"location": {"x": 5, "y": 5}, "properties": ["value1", "value2", "value3"], "order": 4},{"location": {"x": 15, "y": 19}, "properties": ["value1", "value2", "value3"], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 17, "y": 3}, "properties": ["value1", "value2", "value3"], "order": 1},{"location": {"x": 5, "y": 5}, "properties": ["value1", "value2", "value3"], "order": 1},{"location": {"x": 5, "y": 5}, "properties": ["value1", "value2", "value3", ], "order": 2},{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3"], "order": 2},{"location": {"x": 3, "y": 6}, "properties": ["value1", "value2", "value3"], "order": 1},{"location": {"x": 5, "y": 5}, "properties": ["value1", "value2", "value3"], "order": 5}]}}
testDictBad1 = {"game": {"boardSize": 1, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad2= {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "blue", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad3 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "blue", "isNext": False, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad4 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "black", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "white", "isNext": True, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2},{"piece2": {"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}}]}}
testDictBad5 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "white", "isNext": True, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad6 = {"game": {"boardSize": 20, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":4,"y":3}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad7 = {"game": {"boardSize": 20, "player1": {"name": "Vlad", "color": "white", "isNext": True, "nextMove":{"x":21,"y":1}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": False, "nextMove":{"x":0,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad8 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":1,"y":0}}, "listofPiecesPlayer1": [{"location": {"x": 7, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad9 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":1}}, "listofPiecesPlayer1": [{"location": {"x": 7, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}
testDictBad10 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":1}}, "listofPiecesPlayer1": [{"location": {"x": 7, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", ".....", "value3", ".....", "value3", ".....", "value3", ".....", "value3", "....."], "order": 2}]}}
testDictBad11 = {"game": {"boardSize": 7, "player1": {"name": "Vlad", "color": "white", "isNext": False, "nextMove":{"x":0,"y":0}}, "player2": {"name": "Ibrahim", "color": "black", "isNext": True, "nextMove":{"x":0,"y":1}}, "listofPiecesPlayer1": [{"location": {"x": 7, "y": 1}, "properties": ["value1", "value2", "value3", ".....", "value3", ".....", "value3", ".....", "value3", ".....", "value3", "....."], "order": 1}], "listofPiecesPlayer2": [{"location": {"x": 2, "y": 1}, "properties": ["value1", "value2", "value3", "....."], "order": 2}]}}



goodPath = "testData.json"
badPath = "testWrongData.json"
realPath = "gameState.json"


def test_save_game_state():
    assert GameHandler.testSaveGameState(testDictGood1) == 0
    assert GameHandler.testSaveGameState(testDictBad1) == 1
    assert GameHandler.testSaveGameState(testDictGood2) == 0
    assert GameHandler.testSaveGameState(testString) == 1

def test_load_game_state():
    data = GameHandler.testLoadGameState(goodPath)
    assert data["game"]["boardSize"] == 20
    assert data["game"]["player1"]["name"] == "Joachim"
    assert data["game"]["player2"]["color"] == "black"
    assert len(data["game"]["listofPiecesPlayer1"]) == 6

    GameHandler.testSaveGameState(testDictGood1)
    data = GameHandler.testLoadGameState(goodPath)
    assert data["game"]["boardSize"] == 7
    assert data["game"]["player1"]["name"] == "Vlad"
    assert data["game"]["player2"]["isNext"] == True
    assert len(data["game"]["listofPiecesPlayer1"]) == 1
    
    assert GameHandler.testLoadGameState(badPath) == 1

def test_validator():
    assert GameHandler.validateDict(testString) == False
    assert GameHandler.validateDict(testDictBad2) == False
    assert GameHandler.validateDict(testDictBad3) == False
    assert GameHandler.validateDict(testDictBad4) == False
    assert GameHandler.validateDict(testDictBad5) == False
    assert GameHandler.validateDict(testDictBad6) == False
    assert GameHandler.validateDict(testDictBad7) == False
    assert GameHandler.validateDict(testDictBad8) == False
    assert GameHandler.validateDict(testDictBad9) == False
    assert GameHandler.validateDict(testDictBad10) == False
    assert GameHandler.validateDict(testDictBad11) == False
    assert GameHandler.validateDict(testDictGood1) == True
    assert GameHandler.validateDict(testDictGood2) == True

def test_change_file_path():
    config = ConfigParser()
    GameHandler.changeFilePath(badPath)
    config.read("config.ini")
    assert config["DEFAULT"]["path"] == badPath
    GameHandler.changeFilePath(realPath)
    config.read("config.ini")
    assert config["DEFAULT"]["path"] == realPath
    
def test_save_and_load_game_state_with_changed_file_path():
    GameHandler.changeFilePath(goodPath)
    GameHandler.saveGameState(testDictGood1)
    data = GameHandler.loadGameState()
    print(data)
    assert data["game"]["boardSize"] == 7
    assert data["game"]["player1"]["name"] == "Vlad"
    assert data["game"]["listofPiecesPlayer1"][0]["location"]["x"] == 7
    GameHandler.changeFilePath(realPath)
