from Json_Handler import Json_Handler
from queue import Queue
class Playset():
    def __init__(self, jHandler):
        self.rawPlayset = jHandler.getData('playset')
        self.functionList = []

    def convertRaw(self):
        for i in self.rawPlayset:
            function = []
            for e in i:
                function.append(e)
            self.functionList.append(function)


    def __buildEvalString(list):
        evaluationStr = f'{list[0]}('
        for e in list[1:]:
            evaluationStr = evaluationStr + e
        evaluationStr = evaluationStr + ")"
        return evaluationStr

    def actOnIdx(self, idx):
        func = self.__buildEvalString(self.functionList[idx])
        eval(func)

    def runPlayset(self):
        actions = Queue()
        for e in self.functionList:
            actions.put(self.__buildEvalString(e))

        while not actions.empty():
            eval(actions.get())
        
        actions.task_done()
        
