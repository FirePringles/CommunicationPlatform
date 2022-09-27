import Prettify
import numpy as np
import platform
import os

platformName = platform.system()
boring = platformName == "Darwin"

if platformName == "Linux":
    if os.getuid() != 0:
        boring = True

try:
    import keyboard
except:
    boring = True
import sys

class Menu:
    def __init__(self, header, options, width = 0):
        """
            Creates a Menu object that allows the user to pick from multiple choices when run.
            Arguments:
                header: A string to be printed before the options
                options: An list of strings, where the string is the display text for that option.
                width: an int to be used if the width of the menu is to be set manualy
        """
        self.__lastKey = ""
        self.__confirmed = False
        self.header = header
        self.options = options
        self.width = width

    def PrintOptions(self, selectedIndex, width):
        """
            Prints the options with with the option at index selectedIndex having it's colors inverted. width ensures that all lines are at least that width.
            Arguments:
                options: an list strings to be printed for the associated option
                selectedIndex: the currently selected index
                width: the minimum width of each line
        """
        toPrint = ""
        for i in range(len(self.options)):
            text = self.options[i]
            
            if boring:
                text = str(i + 1) + ". " + text

            if(i == selectedIndex):
                print(Prettify.InvertColor(Prettify.CenterText(text, width)))
            else:
                print(Prettify.CenterText(text, width))


    def __GetSelectedModifier(self):
        """
            Reads the keyboard to se if the up or down arrow was pressed. Note that it only triggers once if the key is held down.
            Returns:
                An int with value -1 if up was pressed or 1 if down was pressed
        """
        
        if keyboard.is_pressed('up'):
            if self.__lastKey == 'up':
                return 0
            self.__lastKey = 'up'
            return -1
        elif keyboard.is_pressed('down'):
            if self.__lastKey == 'down':
                return 0
            self.__lastKey = 'down'
            return 1
        
        self.__lastKey = ''
        return 0

    def __GetConfirmation(self):
        """
            Gets if the enter key is pressed. Note that it only triggers once if the key is held down.
            Returns:
                True if enter was pressed and False if not
        """
        if keyboard.is_pressed('enter'):
            if self.__confirmed:
                return False
            input()
            self.__confirmed = True
            return True

        self.__confirmed = False
        return False

    def PrintHeader(self):
        print(self.header)

    def Run(self):
        """
            Prints the Header and allows the user to pick from the options.
            Returns:
                an int which is the index of the selected option
        """
        headerWidth = 0
        if self.width == 0:
            headerWidth = np.max([len(line) for line in self.header.split('\n')])
        else:
            headerWidth = self.width
        selectedIndex = 0
        lastSelectedIndex = 0

        Prettify.ClearScreen()
        self.PrintHeader()
        self.PrintOptions(selectedIndex, headerWidth)

        if boring:
            if len(self.options) == 1:
                input("Press enter to continue")
                return

            first = True
            inputed = -1
            acceptedInputs = range(1, len(self.options) + 1)
            while not inputed in acceptedInputs:
                if not first:
                    print("Not a valid choice")
                try:
                    inputed = int(input("Write the number of your selected option: "))
                except:
                    pass
                first = False
            return inputed - 1


        while True:
            keyboard.read_key()
            if selectedIndex != lastSelectedIndex:
                sys.stdout.write('\033[F' * len(self.options))
                self.PrintOptions(selectedIndex, headerWidth)
            lastSelectedIndex = selectedIndex
            selectedIndex = (selectedIndex + self.__GetSelectedModifier()) % len(self.options)

            if self.__GetConfirmation():            
                return selectedIndex
    
