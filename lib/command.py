import pyautogui
import keyboard
import time
import win32api, win32con
from timers import Timers
class Gamer():
    def _init_(self):
        self.pos = self.getCommandArea()
        if self.pos != None  :
            self.uL = (self.pos.get("x"), self.pos.get("y"))
            self.uR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y"))
            self.dL = (self.pos.get("x"), self.pos.get("y") + self.pos.get("height")) 
            self.dR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y") + self.pos.get("height")) 
        self.timer = {}
        self.actionList = []

    def addTimer(self, key ,timer):
        self.timer.update({key:timer})

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


    def play(self):
        for move in self.actionList:
            move

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

    def clickIfPicture(locat, target):
        if pyautogui.locateOnScreen(locat, grayscale=True, confidence=0.8) != None:
            clickOnPicture(target, 20, 10)
    