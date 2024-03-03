from .jsonHandler import JsonHandler
from queue import Queue
from .actionset import ActionSet
    
class Playset():
    def __init__(self, jHandler, name, gamer):
        self.name = name
        self.game = gamer
        self.rawPlayset = jHandler.getData('playset')
        self.rawActionsets = jHandler.getData('actionset')
        self.actionSets = {}
        self.functionList = []
        self.convertRaw()
        self.actions = Queue()
        self.initActionsets()

    def __str__(self):
        string = f'This is the playeset of:{self.name}\n'
        for idx, i in enumerate(self.functionList):
            string = f'{string}The {idx}. Function: {self.name}.{i[0]}('
            for e in i[1:]:
                if e != i[len(i)-1]:
                    string= f'{string}{e}, '
                else:
                    string= f'{string}{e})\n'
        return string

    def convertRaw(self):
        for i in self.rawPlayset:
            function = []
            for e in i:
                function.append(e)
            self.functionList.append(function)

    def convertRawJson(rawJson):
        out = []
        for i in rawJson:
            function = []
            for e in i:
                function.append(e)
            out.append(function)
        return out
    
    def buildEvalString(self, name, list):
        if list[0] == "conditionalAction":
            evaluationStr = f'{list[0]}(['
            for e in list[1:-3]:
                evaluationStr = evaluationStr + e + ", "
            evaluationStr = evaluationStr + list[-3] + "], "
            evaluationStr = evaluationStr + list[-2] + ", "
            evaluationStr = evaluationStr + list[-1] 
            evaluationStr = f'self.playset.game.{evaluationStr})'    
        else:
            evaluationStr = f'{list[0]}('
            for e in list[1:]:
                if e is not list[-1]:
                    evaluationStr = evaluationStr + e + ", "
                else:
                    evaluationStr = evaluationStr + e
                    
            evaluationStr = f'self.gamers.get("{name}").{evaluationStr})'
    
        return evaluationStr

    def actOnIdx(self, idx):
        func = self.buildEvalString(self.functionList[idx])
        eval(func)

    def queuePlayset(self):
        for e in self.functionList:
            print(f'This is {e}', type(e), f'Name: {self.name}')
            self.actions.put(self.buildEvalString(self.name, e))

    def getQueue(self):
        return self.actions

    def initActionsets(self):
        for e in self.rawActionsets.keys():
            actionset = ActionSet(e, self.convertRawJson(self.rawActionsets.get(e)), self)
            self.actionLists.update(e, actionset)
        


    # def go(self):
    #     while not self.actions.empty():
           
    #         eval(self.actions.get()) 
        
    #     self.actions.task_done()    
        
