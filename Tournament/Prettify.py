import os
import platform

def ClearScreen():
    """Clears the console"""
    operatingSystemName = platform.system();
    if operatingSystemName == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

        
def InvertColor(text):
    """
        Adds tags to the text to invert the text color and text background when printed to the console
        Arguments:
            text: a string
        Returns:
            The text wrapped with the neccessary tags to invert the colors
    """
    return '\x1b[7m' + text + '\x1b[0m'

def CenterText(text, width):
    """
        Adds padding to the left and right of the text to ensure it's length is equal to the width
        Arguments:
            text: a string
            width: an int
        Returns:
            The text with padding added to both sides
    """
    textLength = len(text)
    if(textLength >= width):
        return text

    paddingLeft = int((width - textLength) / 2)
    paddingRight = int(paddingLeft + (width - textLength) % 2)

    return (" " * paddingLeft) + text + (" " * paddingRight)

def PaddCenter(left, right, width):
    """
        Adds padding between left and right so that the minimum length is width
        Arguments:
            left: a string to be placed on left of the padding
            right: a string to be placed on right of the padding
            width: the minimum length of the return string
        Returns:
            A string of the combined left and right strings with padding in the center
    """
    textLength = len(left) + len(right)
    if textLength >= width:
        return left + " " + right
    
    padding = width - textLength
    return left + (" " * padding) + right
