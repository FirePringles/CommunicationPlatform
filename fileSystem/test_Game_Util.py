from gameUtil import GameUtil
from configparser import ConfigParser

testDict = {"game": {
    "boardSize": 25,
    "player1": {
        "name": "Test1",
        "color": "black",
        "isNext": True,
        "nextMove": {
            "x": -1,
            "y": -1
        }
    },
    "player2": {
        "name": "Test2",
        "color": "white",
        "isNext": False,
        "nextMove": {
            "x": -1,
            "y": -1
        }
    },
    "listofPiecesPlayer1": [
            {
            "location": {
                "x": 10,
                "y": 12
            },
            "properties":[
                "value1",
                "value2",
                "value3",
                "....."
            ],
            "order": 1
        },
            {
            "location": {
                "x": 10,
                "y": 12
            },
            "properties":[
                "value1",
                "value2",
                "value3",
                "....."
            ],
            "order": 1
        }
    ],
    "listofPiecesPlayer2": [
            {
            "location": {
                "x": 1,
                "y": 2
            },
            "properties":[
                "value1",
                "value2",
                "value3",
                "....."
            ],
            "order": 1
        },
        {
            "location": {
                "x": 4,
                "y": 3
            },
            "properties":[
                "value1",
                "value2",
                "value3",
                "....."
            ],
            "order": 2
        }

    ],
}}

normalPath = "gameState.json"
testDataPath = "testData.json"

def test_write_file():
    assert GameUtil.testWrite(testDict) != 1

def test_read_file():
    data = GameUtil.testRead("testData.json")
    assert data != 1
    assert len(data["game"]) == 5
    assert len(data["game"]["listofPiecesPlayer1"]) == 2
    assert len(data["game"]["listofPiecesPlayer2"]) == 2
    assert data["game"]["boardSize"] == 25
    assert data["game"]["player1"]["name"] == "Test1"
    assert data["game"]["player1"]["color"] == "black"
    assert data["game"]["player2"]["name"] == "Test2"
    assert data["game"]["player2"]["isNext"] == False
    assert data["game"]["listofPiecesPlayer1"][0]["order"] == 1
    assert data["game"]["listofPiecesPlayer2"][0]["location"]["x"] == 1
    assert data["game"]["listofPiecesPlayer2"][1]["location"]["y"] == 3
    
def test_change_file_path():
    GameUtil.changeFilePath(testDataPath)
    config = ConfigParser()
    config.read("config.ini")
    assert config["DEFAULT"]["path"] == "testData.json"
    GameUtil.changeFilePath(normalPath)