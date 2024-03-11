import queue

from random import randint
from .gamer import Gamer
from .jsonHandler import JsonHandler
from .playset import Playset
from .timers import Timers

class Commander():
    """🎮 Controls the game operations and task management.

    Attributes:
        gamers (dict): A dictionary containing game instances.
        gameQueue (Queue): A queue for game instances.
        queueLength (int): The current length of the game queue.
    """
    def __init__(self):
        self.gamers = {}
        self.gameQueue = queue.Queue(maxsize = 10)
        self.queueLength = self.gameQueue.qsize()

    def __str__(self):
        """📜 Returns a string representation of the Commander."""
        string = f'{self.gamers.get("würfelkingdom")}\n'

        return string

    def generateTimer(self, e):
        """⏱️ Generate timers for a game instance."""
        stop = Timers(5,10)
        long = Timers(10,20)
        key = Timers(0.5, 2)
        click = Timers(0.1, 0.2)
        e.addTimer('long', long)
        e.addTimer('stop', stop)
        e.addTimer('key', key)
        e.addTimer('click', click)

    def addGame(self, gameName):
        """➕ Add a new game to the Commander."""
        newGame = Gamer(gameName)
        self.generateTimer(newGame)
        self.gamers.update({newGame.name:newGame})

    def queueGamer(self, key):
        """ Add a game instance to the game queue."""
        self.gameQueue.put(self.gamers.get(key))
        self.queueLength = self.gameQueue.qsize()

    def playGame(self):
        """▶️ Play a game from the game queue."""
        print("Start Game")
        try:
            current = self.gameQueue.get()
            cQueue = current.getActions()
            while not cQueue.empty():
                currentTask = cQueue.get()
                print(currentTask)
                eval(currentTask) 
            cQueue.task_done() 
            print("Task finished")
            self.queueLength = self.gameQueue.qsize()
        except ValueError as e:
            print(type(e), e)
            print(e.args)
        except Exception as e:
            print(type(e), e)
            print(e.args)


    def scanTasks(self):
        """🔍 Scan for new tasks and manage the game queue."""
        if self.queueLength == 0:
            print("No new tasks, choosing random Task!")
            self.queueGamer(list(self.gamers.keys())[randint(0,len(self.gamers)-1)])
        elif self.queueLength < 10:
            print("Getting next Task")
            self.queueGamer(self.nextTask())


    def nextTask(self): ## TODO for future update implement scheduler with async timer
        """🔄 Retrieve the next task."""
        result = "würfelkingdom"
        print(f"Found new Task: {result}")
        return result

    def getGamer(self):
        pass

    def gameLoop(self, key):
        """🔄 Run the game loop."""
        while key or self.queueLength != 0:
            print("Scanning for new Tasks.")
            self.scanTasks()
            self.playGame()
        if not key:
            print("Ending Loop!")
            print(f"Finishing Tasks: {self.gameQueue}")
                
    
    def killBot(self):
        """🔄 Run the game loop."""
        pass 



    #"function": {
    #   "arg1": 229,
    #   "arg2": 115,
    #   "argN": ...,
    # },

    # {
    #   "name" = "function":
    #   "arg1": 229,
    #   "arg2": 115,
    #   "argN": ...,
    # },


        
