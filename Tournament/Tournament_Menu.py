import Tournament
import Menu
import Prettify
import platform
import sys
import os

platformName = platform.system()
boring = platformName == "Darwin"

if platformName == "Linux":
    if os.getuid() != 0:
        boring = True

if not boring:
    try:
        import keyboard
    except:
        boring = True

minPlayers = 3
maxPlayers = 8

playerNumberChoices = range(minPlayers, maxPlayers + 1)

maxNameLength = 12

def NewTournament():
    """
        Starts a new tournament.
    """
    opts = [str(i) for i in playerNumberChoices]
    m = Menu.Menu("Choose number of players:", opts)
    i = m.Run()
    names = NamePlayers(playerNumberChoices[i])
    
    t = Tournament.Tournament(names)

    t.playTournament()

    return

def PrintPlayerNames(playerNames, selectedIndex):
    """
    Prints the current player names, with the name at selectedIndex being highlighted.
    Arguments:
        playerNames: an list of strings of the player names.
        selectedIndex: an int of what index should be highlighted.
    """
    for i in range(len(playerNames)):
        text = playerNames[i] + "_" * (maxNameLength - len(playerNames[i]))
        if selectedIndex == i:
            print(Prettify.InvertColor(text))
        else:
            print(text)

def PrintConfirm(selected, width):
    """
        Prints the Continue option.
        Arguments:
            selected: a bool if it should be highlighted.
            width: the minimum width of the continue option.
    """
    if selected:
        print(Prettify.InvertColor(Prettify.CenterText("Continue", width)))
    else:
        print(Prettify.CenterText("Continue", width))

lastKey = ""
def GetSelectedModifier():
    """
        Reads the keyboard to se if the up or down arrow was pressed. Note that it only triggers once if the key is held down.
        Returns:
            An int with value -1 if up was pressed or 1 if down was pressed
    """
    global lastKey
    if keyboard.is_pressed('up'):
        if lastKey == 'up':
            return 0
        lastKey = 'up'
        return -1
    elif keyboard.is_pressed('down'):
        if lastKey == 'down':
            return 0
        lastKey = 'down'
        return 1
    
    lastKey = ''
    return 0

confirmed = False
def GetConfirmation():
        """
            Gets if the enter key is pressed. Note that it only triggers once if the key is held down.
            Returns:
                True if enter was pressed and False if not
        """
        global confirmed
        if keyboard.is_pressed('enter'):
            if confirmed:
                return False
            buff = input()
            sys.stdout.write('\033[F')
            print(" " * len(buff))

            confirmed = True
            return True

        confirmed = False
        return False

backspaced = False
def NewPlayerName(current, key):
    """
        Returns the new name of the player depending on the key.
        Arguments:
            current: a string which is the current name of the player.
            key: a string which is the current key pressed or released.
        Returns:
            A string of the new name.
    """
    global backspaced
    ret = current
    if len(str(key)) == 1 and keyboard.is_pressed(key):

        ret += key
    if keyboard.is_pressed('backspace'):
        if backspaced:
            ret[0:maxNameLength]
        backspaced = True
        if keyboard.is_pressed('ctrl'):
            return ""
        return ret[0:(len(ret)-1)]

    return ret[0:maxNameLength]

def ValidNames(playerNames):
    """
    Checks if the player names are valid
    Arguments:
        An list of strings that are the player names.
    Returns:
        A tuple (bool, string) where the bool is if the names are valid and the string is the reason they are invalid or empty
    """
    otherNames = []
    for name in playerNames:
        if len(name) == 0 or len(name) > maxNameLength:
            return (False, "All Players must have a name!")
        if name in otherNames:
            return (False, "Players can't have the same names")
        otherNames.append(name)
    return (True, "")

def NamePlayers(numberOfPlayers):
    """
        Gets the name of every player from the user.
        Arguments:
            numberOfPlayers: a int which is the number of names to be inputed.
        Returns:
            A list of strings which are the inputed names.
    """
    global lastKey
    global confirmed
    global backspaced
    lastKey = ""
    confirmed = False
    backspaced = False
    Prettify.ClearScreen()
    playerNames = ["" for _ in range(numberOfPlayers)]
    selectedIndex = 0
    lastIndex = 0
    width = max(maxNameLength, len("Enter Names:"))
    print("Enter Names:")

    if boring:
        for i in range(numberOfPlayers):
            while True:
                name = input("Player " + str(i + 1) + " Name: ")
                if len(name) == 0:
                    print("Name can't be empty")
                    continue
                if len(name) > maxNameLength:
                    print("Name is to long must be under " + str(maxNameLength) + " characters")
                    continue
                if name in playerNames:
                    print("Players cannot share names")
                    continue
                playerNames[i] = name
                break

        return playerNames

    PrintPlayerNames(playerNames, selectedIndex)
    PrintConfirm(selectedIndex == (len(playerNames) + 1), width)
    while True:
        key = keyboard.read_key()
        if lastIndex != selectedIndex:
            sys.stdout.write('\033[F' * (len(playerNames) + 1))
            PrintPlayerNames(playerNames, selectedIndex)
            PrintConfirm(selectedIndex == (len(playerNames)), width)

        lastIndex = selectedIndex
        selectedIndex = (selectedIndex + GetSelectedModifier()) % (len(playerNames) + 1)

        if GetConfirmation():
            sys.stdout.write('\033[F')
            if selectedIndex < len(playerNames):
                selectedIndex = (selectedIndex + 1) % (len(playerNames) + 1)
            else:
                (valid, error) =ValidNames(playerNames)
                if valid:
                    return playerNames
                else:
                    msg = error + "(press any key to continue)"
                    print(msg)
                    k = keyboard.read_key()
                    while not keyboard.is_pressed(k):
                        k = keyboard.read_key()

                    if k == "enter":
                        input()
                        sys.stdout.write('\033[F')
                    
                    sys.stdout.write('\033[F')
                    print(" " * len(msg))
                    sys.stdout.write('\033[F')

        if selectedIndex < len(playerNames):
            prev = playerNames[selectedIndex]
            playerNames[selectedIndex] = NewPlayerName(playerNames[selectedIndex], key)

            if prev != playerNames[selectedIndex]:
                lastIndex = -1

