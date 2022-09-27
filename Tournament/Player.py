class Player:

  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.score = 0
    self.lastPlayedPiece = None
    self.numOfWhitePlayed = 0
    self.numOfBlackPlayed = 0
    self.isActive = None