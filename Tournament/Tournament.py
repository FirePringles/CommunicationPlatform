import Player
import MatchSchedule
import random
import Leaderboard
import Menu
import Prettify

class Tournament:

  def __init__(self, playerNamesList):
    """
      Creates a Tournament object that allows to start a tournament.
      Arguments:
        playerNamesList: A list of player names who are to participate in the tournament 
    """
    self.playerNamesList = playerNamesList
    self.schedule = []

  def createListOfPlayers(self):
    """
      Creates a list of Player object from the playerNameList who are to play the tournament
    """
    playersList = []
    id = 1
    for playerName in self.playerNamesList:
      player = Player.Player(playerName, id)
      player.isActive = True
      playersList.append(player)
      id += 1
    
    return playersList
  
  def setPlayingPiece(self, player1, player2):
    """
      Chooses the playing piece for two given players. The playing piece is either White or Black
      Arguments:
          player1: a player object to choose the playing piece for
          player2: a player object to choose the playing piece for
    """

    if(player1.lastPlayedPiece == None and player2.lastPlayedPiece == None):
       player1.lastPlayedPiece = "White"
       player1.numOfWhitePlayed += 1
       player2.lastPlayedPiece = "Black" 
       player2.numOfBlackPlayed += 1

    elif(player1.lastPlayedPiece == "White" and player2.lastPlayedPiece == None):
        player1.lastPlayedPiece = "Black"
        player1.numOfBlackPlayed += 1
        player2.lastPlayedPiece = "White"
        player2.numOfWhitePlayed += 1

    elif(player1.lastPlayedPiece == "Black" and player2.lastPlayedPiece == None):
        player1.lastPlayedPiece = "White"
        player1.numOfWhitePlayed += 1
        player2.lastPlayedPiece = "Black"
        player2.numOfBlackPlayed += 1

    elif(player1.lastPlayedPiece == None and player2.lastPlayedPiece == "White"):
        player1.lastPlayedPiece = "White"
        player1.numOfWhitePlayed += 1
        player2.lastPlayedPiece = "Black"
        player2.numOfBlackPlayed += 1

    elif(player1.lastPlayedPiece == None and player2.lastPlayedPiece == "Black"):
        player1.lastPlayedPiece = "Black"
        player1.numOfBlackPlayed += 1
        player2.lastPlayedPiece = "White"
        player2.numOfWhitePlayed += 1
    
    elif(player1.lastPlayedPiece == "White" and player2.lastPlayedPiece == "Black"):
        player1.lastPlayedPiece = "Black"
        player1.numOfBlackPlayed += 1
        player2.lastPlayedPiece = "White"
        player2.numOfWhitePlayed += 1

    elif(player1.lastPlayedPiece == "Black" and player2.lastPlayedPiece == "White"):
        player1.lastPlayedPiece = "White"
        player1.numOfWhitePlayed += 1
        player2.lastPlayedPiece = "Black"
        player2.numOfBlackPlayed += 1

    elif(player1.lastPlayedPiece == "White" and player2.lastPlayedPiece == "White"):
        if(player1.numOfBlackPlayed > player2.numOfBlackPlayed):
            player1.lastPlayedPiece = "White"
            player1.numOfWhitePlayed += 1
            player2.lastPlayedPiece = "Black"
            player2.numOfBlackPlayed += 1
        else:
           player1.lastPlayedPiece = "Black"
           player1.numOfBlackPlayed += 1
           player2.lastPlayedPiece = "White"
           player2.numOfWhitePlayed += 1

    
    elif(player1.lastPlayedPiece == "Black" and player2.lastPlayedPiece == "Black"):
        if(player1.numOfWhitePlayed > player2.numOfWhitePlayed):
            player1.lastPlayedPiece = "Black"
            player1.numOfBlackPlayed += 1
            player2.lastPlayedPiece = "White"
            player2.numOfWhitePlayed += 1
        else:
           player1.lastPlayedPiece = "Black"
           player1.numOfBlackPlayed += 1
           player2.lastPlayedPiece = "White"
           player2.numOfWhitePlayed += 1
    else: 
      return

  def createMatches(self, playerList):
    """
      Creates a list of matches that are to be played and stores the resulting list in the tournament object attribute schedule which is a list of MatchSchedule objects.
      Argument:
      playerList: a list of Player object from whom the match schedule is to be created from.
    """
    numberOfPlayers = len(playerList)

    for x in range(numberOfPlayers - 1):
      for y in range(x + 1, numberOfPlayers):
        matchId = (playerList[x].id, playerList[y].id)
        matchSchedule = MatchSchedule.MatchSchedule(matchId)
        self.schedule.append(matchSchedule)


    random.shuffle(self.schedule)
 
  def getNextMatch(self, playerList):
    """
      Gets the 2 Players from the schedule who are to play next match, if all matches are done, it returns an empty list.
      Argument:
          playerList: a list of Player object to get the players who are to play next.
    """
    
    for match in self.schedule:
      if(not(match.done) and not(match.forfeit)):
        players = [player for player in playerList if player.id == match.idTuple[0] or player.id == match.idTuple[1]]
        return players
    
    return []

  def playMatch(self, players):
      """
        Plays the match between the 2 players, by first setting the playing piece and updating the player score
        Argument:
          players: A list of 2 Player object who are to play the match
      """
      match = [match for match in self.schedule if match.idTuple[0] == players[0].id and match.idTuple[1] == players[1].id]
      self.setPlayingPiece(players[0], players[1])
      
      #TODO: placeholder should be replaced with playing a game
      m = Menu.Menu("Select winner:", [p.name for p in players])
      winningPlayer = players[m.Run()]
      winningPlayer.score += 1
      #TODO: end of placeholder

      match[0].done = True
      
  
  def updateSchedule(self, player):
    """
      Updates the schedule of the Tournament object when one player forfeits. The status of the match forfeit is set to true.
      Argument:
        player: A player object who has forfeited the tournament.
    """
    matches = list(filter(lambda match: player.id in match.idTuple, self.schedule))
    for match in matches:
      match.forfeit = True


  def updateScore(self, player, playerList):
    """
      Updates the score for all opposing players who were to play the player who forfeited.
      Arguments:
        player: A player object who has forfeited.
        playerList: A list of all player object.
    """
    matches = list(filter(lambda match: player.id in match.idTuple, self.schedule))
    for match in matches:
      for i in range(0,2):
        if(match.idTuple[i] != player.id):
          playerToUpdate = list(filter(lambda x: x.id == match.idTuple[i],playerList))
          if playerToUpdate[0].isActive:
            playerToUpdate[0].score += 1
  
  def forfeit(self, playerName, playerList):
    """
    Updates the schedule, score and status when a player forfeits.
    Arguments:
      playerName: A player object who has forfeited.
      playerList: A list of all player object to update the score for.
    """
    player = [player for player in playerList if player.name == playerName]
    player[0].isActive = False
    self.updateSchedule(player[0])
    self.updateScore(player[0], playerList)


  def tieBreaker(self, playerList):
    """
    Runs the iteration of round robin tournament when a tiebreaker scenario is met.
    Argument:
      playerList: A list of player object whom are to play the iteration of round robin again. 
    """
    self.createMatches(playerList)
    self.playTournamentWithPlayers(playerList)
    return self.chooseWinner(playerList)

  def chooseWinner(self, playersList):
   """
   Determines the winner of the tournament by choosing the highest scoring player and calls tiebreaker function if there are multiple players with the high score.
   Argument:
    playersList: A list of player object to choose the winner from.
   """
   maxScore = max(player.score for player in playersList)
   playersWithMaxScore = list(filter(lambda player: player.score == maxScore, playersList))
   if(len(playersWithMaxScore) > 1):
     return self.tieBreaker(playersWithMaxScore)
   
   return playersWithMaxScore[0]
  

  def playTournamentWithPlayers(self, playerList):
    """
    Starts the tournament by creating matches and playing matches and returns a winner for the tournament
    Argument:
      playerList: A list of player object who are going to play the tournament
    """
    self.createMatches(playerList)
    playersToPlay = self.getNextMatch(playerList)
    while True:
      if len(playersToPlay) == 0:
        return self.chooseWinner(playerList)

      playersffs = [p for p in playersToPlay]
      while True:
        if len(playersffs) == 0:
          break
        opts = [p.name + " forfeits" for p in playersffs]
        opts.append("Continue")
        fMenu = Menu.Menu("Does any of the players for the ", opts)
        c = fMenu.Run()
        if c == len(opts) - 1:
          break
        playerToff = playersffs[c]
        playersffs.remove(playerToff)
        self.forfeit(playerToff.name, playerList)

      if playersToPlay[0].isActive and playersToPlay[1].isActive:
        self.playMatch(playersToPlay)

      Leaderboard.DisplayLeaderboard(playerList)

      playersToPlay = self.getNextMatch(playerList)

  def playTournament(self):
    """
    Calls the playTournamentWithPlayers function to start the tournament and prints out the winner to user.
    """
    winner = self.playTournamentWithPlayers(self.createListOfPlayers())

    header = Prettify.CenterText("THE WINNER IS:", 20)
    wName = Prettify.InvertColor(Prettify.CenterText(winner.name, 20))
    m = Menu.Menu(header + "\n" + wName + "\n", ["End Tournament"], 20)
    m.Run()