import Menu
import Prettify
import Player

width = 20

def DisplayLeaderboard(playerStatStuff):
    sortedList = sorted(playerStatStuff, key=lambda player: player.score, reverse=True)
    header = Prettify.InvertColor(Prettify.CenterText("Leaderboard", width)) + '\n'
    for i in range(len(sortedList)):
        player = sortedList[i]
        if i % 2 == 0:
            header += Prettify.PaddCenter(" " + player.name, str(player.score) + " ", width) + "\n"
        else:
            header += Prettify.InvertColor(Prettify.PaddCenter(" " + player.name, str(player.score) + " ", width)) + "\n"

    m = Menu.Menu(header, ["Continue"], width)
    m.Run()
