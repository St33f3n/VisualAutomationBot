from Json_Handler import Json_Handler
from queue import Queue
class Playset():
    def __init__(self, jHandler, name):
        self.name = name
        self.rawPlayset = jHandler.getData('playset')
        self.functionList = []
        self.convertRaw()
        self.actions = Queue()

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


    def __buildEvalString(name, list):
        evaluationStr = f'{list[0]}('
        for e in list[1:]:
            evaluationStr = evaluationStr + e
        evaluationStr = f'{name}.{evaluationStr})'
        return evaluationStr

    def actOnIdx(self, idx):
        func = self.__buildEvalString(self.functionList[idx])
        eval(func)

    def queuePlayset(self):
        for e in self.functionList:
            self.actions.put(self.__buildEvalString(self.name, e))

    def go(self):
        while not self.actions.empty():
            eval(self.actions.get())
        
        self.actions.task_done()    
        
