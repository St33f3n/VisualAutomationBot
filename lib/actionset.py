from queue import Queue
from .playset import *
class ActionSet():
    def __init__(self, name, data, playset):
        self.name = name
        self.functionList = data
        self.playset = playset
        self.instructions = self.initInstructionQueue()


    def initInstructionQueue(self):
        out = Queue()
        for e in self.functionList:
            out.put(self.playset.buildEvalString(self.playset.name, e))
        return out
    
    def runActionset(self):
        if self.instructions.empty():
            self.instructions = self.initInstructionQueue()

        while not self.instructions.empty():
            currentInstruction = self.instructions.get()
            print(currentInstruction)
            eval(currentInstruction)

        print(f"Actionset {self.name} done!")