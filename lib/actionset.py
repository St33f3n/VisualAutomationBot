from queue import Queue
from .playset import *
class ActionSet():
    """🎬 Represents a set of actions to be executed.

    Args:
        name (str): The name of the action set.
        data (list): A list of function names.
        playset (PlaySet): The playset associated with this action set.
    
    Attributes:
        name (str): The name of the action set.
        functionList (list): A list of function names.
        playset (PlaySet): The playset associated with this action set.
        instructions (Queue): A queue containing the instructions for the action set.
    """

    def __init__(self, name, data, playset):
        self.name = name
        self.functionList = data
        self.playset = playset
        self.instructions = self.initInstructionQueue()


    def initInstructionQueue(self):
        """🛠️ Initialize the instruction queue."""
        out = Queue()
        for e in self.functionList:
            out.put(self.playset.buildEvalString(self.playset.name, e))
        return out
    
    def runActionset(self):
        """🏃‍♂️ Run the action set."""
        if self.instructions.empty():
            self.instructions = self.initInstructionQueue()

        while not self.instructions.empty():
            currentInstruction = self.instructions.get()
            print(currentInstruction)
            eval(currentInstruction)

        print(f"Actionset {self.name} done!")