import queue

from regex import E
from .gamer import Gamer
from .jsonHandler import JsonHandler
from .playset import Playset
from .timers import Timers

class Commander():
    def __init__(self):
        self.gamers = {}
        self.gameQueue = queue.Queue(maxsize = 10)
        self.queueLength = self.gameQueue.qsize()

    def __str__(self):
        
        string = f'{self.gamers.get("würfelkingdom")}\n'

        return string

    def generateTimer(self, e):
        stop = Timers(1,3)
        key = Timers(0.5, 2)
        click = Timers(1, 2)
        e.addTimer('stop', stop)
        e.addTimer('key', key)
        e.addTimer('click', click)

    def addGame(self, gameName):
        newGame = Gamer(gameName)
        self.generateTimer(newGame)
        self.gamers.update({newGame.name:newGame})

    def queueGamer(self, key):
        self.gameQueue.put(self.gamers.get(key))

    def playGame(self):
        try:
            current = self.gameQueue.get()
            cQueue = current.getActions()
            while not cQueue.empty():
                currentTask = cQueue.get()
                print(currentTask)
                eval(currentTask) 
            cQueue.task_done() 
            self.checkTimers()
        except ValueError as e:
            print(e)


    def checkTimers(self):
        return 0
    
    def getGamer(self):
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


        
