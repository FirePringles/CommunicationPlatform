import time
import Menu
import Tournament_Menu

def testF():
    print('Leaving')
    time.sleep(1)
    exit()
        

menuOpts = [
    "Start New Game",
    "Start New Tournament",
    "Load Game",
    "Exit"
]

actions = [
    lambda: print('Started New Game...'),
    lambda: Tournament_Menu.NewTournament(),
    lambda: print('Loading Game...'),
    testF
]

title = """
  _    _ _    _    _____                       
 | |  | | |  | |  / ____|                      
 | |  | | |  | | | |  __  __ _ _ __ ___   ___  
 | |  | | |  | | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |__| | |__| | | |__| | (_| | | | | | |  __/ 
  \____/ \____/   \_____|\__,_|_| |_| |_|\___| 
                                              """

m = Menu.Menu(title, menuOpts)


while True:
    ret = m.Run()
    actions[ret]()
    
