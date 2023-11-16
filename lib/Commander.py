import queue
from lib.Gamer import Gamer
from lib.Json_Handler import Json_Handler
from lib.Playset import Playset
from lib.timers import Timers

class Commander():
    def __init__(self):
        self.gamers = {}
        self.gameQueue = queue.Queue(maxsize = 10)
        self.queueLength = self.gameQueue.qsize()
        
    def generateTimer(self):
        stop = Timers(1,3)
        key = Timers(0.5, 2)
        click = Timers(1, 2)
        for e in self.gamers:
            e.addTimer('stop', stop)
            e.addTimer('key', key)
            e.addTimer('click', click)

    def addGame(self, gameName):
        newGame = Gamer(gameName)
        self.gamers.update({newGame.name:newGame})

    def queueGamer(self, key):
        self.gameQueue.put(self.gamers.get(key))

    def playGame(self):
        current = self.gameQueue.get()
        while not current.play(): 
            x = current.play()
            self.checkTimers()

    def checkTimers(self):
        return 0
    
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


        