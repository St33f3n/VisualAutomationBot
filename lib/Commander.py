import queue
from Gamer import Gamer
from Json_Handler import Json_Handler

class Commander():
    def __init__(self):
        self.gamers = {}
        self.gameQueue = queue.SimpleQueueQueue(maxsize = 10)
        self.queueLength = self.gameQueue.qsize()
        

    def addGamer(self, gameName):
        newGame = Gamer(gameName)
        self.gamers.update(newGame.name, newGame)

    def playGame(self):
        current = self.gameQueue.get()
        while not x: 
            x = current.play()
            self.checkTimers()

    def buildPlayset(self):
        playset = Json_Handler.getData('playset')

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


        