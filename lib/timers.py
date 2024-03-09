import random
from numpy import random as rand
import time


class Timers():
    """
    Represents a set of timers for random waiting periods.

    Attributes:
        minimal_duration (float): The minimum duration for timers.
        maximal_duration (float): The maximum duration for timers.
        lifetime (list): List containing lifetimes for each timer.
    """
    def __init__(self, mindur, maxdur):
        """
        Initializes Timers object.

        Args:
            mindur (float): The minimum duration for timers.
            maxdur (float): The maximum duration for timers.
        """
        self.minimal_duration = mindur
        self.maximal_duration = maxdur
        self.lifetime = [ self.createLifetime() for x in range(0,9)]
        

    def __str__(self):
        """
        Returns a string representation of the Timers object.

        Returns:
            str: String representation of the Timers object.
        """
        return f'Range from: {self.minimal_duration}-{self.maximal_duration}\nCurrent waitTime: {self.lifetime}'

    def createLifetime(self):
        """
        Creates a random lifetime for a timer.

        Returns:
            float: Random lifetime value.
        """
        return rand.uniform(self.minimal_duration, self.maximal_duration)

    def hPause(self):
        """
        Pauses execution for a random duration specified by the timers.
        """
        time.sleep(self.lifetime[random.randint(0,9)])



