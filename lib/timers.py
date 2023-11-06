from numpy import random as rand
import time


class timers():
    def _init_(self, mindur, maxdur):
        self.minimal_duration = mindur
        self.maximal_duration = maxdur
        self.lifetime = self.createLifetime()

    def createLifetime()
        return rand.uniform(self.minimal_duration, self.maximal_duration)

    def hPause()
        time.sleep(self.lifetime)
