# File System
The goal of the Filysystem package is to enable saving and loading of the UUGame. The Gamestate will be saved and loaded in a .json file in this folder. The file will be stored in this directory and this can be changed using the game.config file. 

## Requirements
* `configparser`
* `asyncore`
* `configparser`

## Structure
* `gameHandler.py` the main library that is used to call saveGameState(gameDict) and loadGameState()
* `gameUtil.py` class that contains helper functions for the main class GameHandler

## Functions
* `saveGameState(gameDict)` Saves the current gamestate and stores the data in gameState.json. 
* `loadGameState()` Returns the gameState data in the format that can be seen in the section "Format of the gameDict input". The filepath is by default gameState.json and is saved in this directory. The filepath game be changed in game.config

## Usage And Examples
1. Import the GameHandler class 
```
from gameHandler importGameHandler

```
2. Convert the game data to the required format that can be seen in the section "Format of the gameDict input"
```
gameDict = {"game": {
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
```
3. Save the gameState and store the data in the file gameState.json
```
GameHandler.saveGameState(gameDict) 
```

4. Load the gameState. The loaded file will be the one specified in game.config. Default path is gameState.json in this directory. The data in this example will have the format specified in the section "Format of the gameDict input"
```
data = GameHandler.loadGameState()
```
## Format of the gameDict input 
```
gamedict = {"game": {
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

```
