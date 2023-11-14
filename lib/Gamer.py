import random
import pyautogui, json, os, keyboard, time, cv2
import win32api, win32con
from lib.oldBot import picToCoordinates
from timers import Timers
import ocr ,Json_Handler


class Gamer():
    def _init_(self, name):
        self.name = name
        self.pos = self.getCommandArea()
        if self.pos != None  :
            self.uL = (self.pos.get("x"), self.pos.get("y"))
            self.uR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y"))
            self.dL = (self.pos.get("x"), self.pos.get("y") + self.pos.get("height")) 
            self.dR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y") + self.pos.get("height")) 
        self.timer = {}
        self.playset = None
        json_handler = Json_Handler(name)

    def addTimer(self, key ,timer):
        self.timer.update({key:timer})

    def loadData(self):
        with open(f'{self.name}/info.json', 'r') as f:
            self.jsonData = json.load(f)

    def saveData(self, key):
        # TODO data is comming, need to be converted to json and saves back.
        None

    def getPictureData(self, key):
        if key in self.jsonData['pictures']:
            localData = self.jsonData['pictures'][key]
            w = localData['width']
            h = localData['height']
            p = localData['path']
            return (w, h, p)
        
    def getDataData(self, key):
        if key in self.jsonData['data']:
            localData = self.jsonData['data'][key]
            v = localData['value']
            sx = localData['size']['x']
            sy = localData['size']['y']
            return (v, sx, sy) 

    def getCommandArea(self):
        print("Select the upper left edge on wich you want to start the bot.\nPress c to capture the edge.")
        while keyboard.is_pressed('c') is False:
            time.sleep(0.1)
            print(".", " ")
        upperEdge = pyautogui.position()
        print("Select the lower right edge on wich you want to start the bot.\nPress c to capture the edge.")
        while keyboard.is_pressed('c') is False:
            time.sleep(0.1)
        lowerEdge = pyautogui.position()
        winPos = {"x" : upperEdge[0], "y" : upperEdge[1], "width" : lowerEdge[0]-upperEdge[0], "height": lowerEdge[1]-upperEdge[1]}
        print(f"Window at: {winPos} captured!")
        if lowerEdge != None and upperEdge != None:
            return winPos
        else:
            return None


    def play(self): ##TODO
        action = self.playset
        action
        return self.actionList.empty()

    def simpleClick(self, x, y):
        if x in range(self.uL[0],self.uR[0]) and y in range(self.uL[1],self.dR[1]):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            self.timer.get("clicktimer").hpause()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        else:
            print("out of window")

    def keyPress(self, key):
        pyautogui.keyDown(key)
        self.timer.get("keytimer").hpause()
        pyautogui.keyUp(key)

    def clickIfPicture(self, key1, key2):
        """key1 = Ziel das erkannt werden soll\n
        key2 = Ziel auf das gedrückt wird"""

        target1 = self.json_handler.getData(key1)
        if pyautogui.locateOnScreen(target1[2], grayscale=True, confidence=0.8) != None:
            self.clickOnPicture(key2)
        else:
            print("Picture not found!\nMaybe the sequenze is messed up?")
    
    def clickOnPicture(self, key):
        target = picToCoordinates(key)
        if target != None:
            self.simpleClick(target[0],target[1])
            return True 
        else:
            return False
        
    def picToCoordinates(self, key):
        width , height, path = self.getPictureData(key)
        location = pyautogui.locateOnScreen(path, grayscale=True, confidence=0.8)
        rndPoint = (random.randint(location[0],location[0]+width), random.randint(location[1], location[1]+height))
        return rndPoint
    
    def locateRessources(self, key):
        width , height, path = self.getPictureData(key)
        value, sizeX, sizeY = self.getDataData(key)
        location = pyautogui.locateOnScreen(path, grayscale=True, confidence=0.8)

        region = (location[0] + location[2], location[1], sizeX, location[3])
        data = ocr.ocr(region)

        self.saveData(data, key)


    

