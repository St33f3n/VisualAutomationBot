import queue

from random import randint
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
        self.queueLength = self.gameQueue.qsize()

    def playGame(self):
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
        if self.queueLength == 0:
            print("No new tasks, choosing random Task!")
            self.queueGamer(self.gamers.keys[randint(0,self.gamers.length())])
        elif self.queueLength < 10:
            print("Getting next Task")
            self.queueGamer(self.nextTask())


    def nextTask(self): ## TODO for future update implement scheduler with async timer
        result = "würfelkingdom"
        print(f"Found new Task: {result}")
        return result

    def getGamer(self):
        pass

    def gameLoop(self, key):
        while key :
            print("Scanning for new Tasks.")
            self.scanTasks()
            self.playGame()
        while not key  & self.queueLength != 0:
            print("Ending Loop!")
            print(f"Finishing Tasks: {self.gameQueue}")
            self.playGame()
    
    def killBot(self):
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


        
