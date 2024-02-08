class ActionSet():
    def __init__(self, name, data):
        self.name = name
        self.rawActionset = data
        self.functionList = self.convertRaw


