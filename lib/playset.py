from .jsonHandler import JsonHandler
from queue import Queue
from .actionset import ActionSet
    
class Playset():
    """
    Represents a playset of actions to be performed in a game.

    Attributes:
        jHandler (JsonHandler): The JSON handler object.
        name (str): The name of the playset.
        gamer (str): The name of the gamer.
        rawPlayset (dict): The raw playset data.
        rawActionsets (dict): The raw actionset data.
        actionSets (dict): Dictionary containing ActionSet objects.
        functionList (list): List containing function information.
        actions (Queue): Queue to store actions.
    """
    def __init__(self, jHandler, name, gamer):
        """
        Initializes a Playset object.

        Args:
            jHandler (JsonHandler): The JSON handler object.
            name (str): The name of the playset.
            gamer (str): The name of the gamer.
        """
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
        """
        Returns a string representation of the Playset object.

        Returns:
            str: String representation of the Playset.
        """
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
        """
        Converts raw playset data to a function list.
        """
        for i in self.rawPlayset:
            function = []
            for e in i:
                function.append(e)
            self.functionList.append(function)

    def convertRawJson(rawJson: list):
        """
        Converts raw JSON data to a function list.

        Args:
            rawJson (list): Raw JSON data.

        Returns:
            list: Function list.
        """
        out = []
        for i in rawJson:
            function = []
            for e in i:
                function.append(e)
            out.append(function)
        return out
    
    def buildEvalString(self, name: str, list: list):
        """
        Builds an evaluation string for function execution.

        Args:
            name (str): The name of the function.
            lst (list): The list containing function arguments.

        Returns:
            str: Evaluation string.
        """
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

    def actOnIdx(self, idx: int):
        """
        Executes an action based on the index.

        Args:
            idx (int): The index of the action to execute.
        """
        func = self.buildEvalString(self.functionList[idx])
        eval(func)

    def queuePlayset(self):
        """
        Queues all functions in the playset.
        """
        for e in self.functionList:
            print(f'This is {e}', type(e), f'Name: {self.name}')
            self.actions.put(self.buildEvalString(self.name, e))

    def getQueue(self):
        """
        Gets the queue of actions.

        Returns:
            Queue: The queue of actions.
        """
        return self.actions

    def initActionsets(self):
        """
        Initializes action sets.
        """
        for e in self.rawActionsets.keys():
            actionset = ActionSet(e, self.convertRawJson(self.rawActionsets.get(e)), self)
            self.actionLists.update(e, actionset)
        


    # def go(self):
    #     while not self.actions.empty():
           
    #         eval(self.actions.get()) 
        
    #     self.actions.task_done()    
        
