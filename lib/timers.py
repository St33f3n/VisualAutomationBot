import random
from numpy import random as rand
import time


class Timers():
    def __init__(self, mindur, maxdur):
        self.minimal_duration = mindur
        self.maximal_duration = maxdur
        self.lifetime = [ self.createLifetime() for x in range(0,9)]
        

    def __str__(self):
        return f'Range from: {self.minimal_duration}-{self.maximal_duration}\nCurrent waitTime: {self.lifetime}'

    def createLifetime(self):
        return rand.uniform(self.minimal_duration, self.maximal_duration)

    def hPause(self):
        time.sleep(self.lifetime[random.randint(0,9)])



