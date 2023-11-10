import pyautogui
import keyboard
import time
import win32api, win32con
class commander:
    def _init_(self):
        self.winID = wi.get_active_window().id
        self.pos = self.getCommandArea()
        self.uL = (self.pos.x, self.pos.y)
        self.uR = (self.pos.x + self.pos.width, self.pos.y)
        self.dL = (self.pos.x, self.pos.y + self.pos.height)
        self.dR = (self.pos.x + self.pos.width, self.pos.y + self.pos.height)
        self.actionList = []

    def getCommandArea():
        print("Select the window on wich you want to start the bot.\nPress c to capture the window.")
        while keyboard.is_pressed('c') is False:
            time.sleep(0.1)
            print(".", " ")
        win = wi.get_active_window
        winPos = wi.get_absolute_geometry(win)
        print("Window at: " + winPos + " captured!")
        return winPos

    def play(self):
        for move in self.actionList:
            move

    def simpleClick(self, x, y):
        if x in range(self.uL[0],self.uR[0]) and y in range(self.uL[1],self.dR[1]):
            pyautogui.leftClick(x,y)
        

