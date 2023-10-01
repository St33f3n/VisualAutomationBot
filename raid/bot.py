from PIL import Image
from pytesseract import *
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

startFight = [(1060, 1100), (666,720)]
kampagne = [(30, 220), (140, 650)]
Chars = [[(50, 100), (525, 610)], [(50-100), (640, 730)], [(140, 190), (525, 610)], [(140,190),(640- 730)], [(230, 280), (525, 610)]]
nextLevel = [(1050, 1200), (666, 719)]
start = [(1000, 1200), (640, 710)]

def click(coordinates, stop):
	win32api.SetCursorPos(coordinates)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(np.random.uniform(stop, 2*stop))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	

def keyPress(key, stop):
	pyautogui.keyDown(key)
	time.sleep(np.random.uniform(stop, 2*stop))
	pyautogui.keyUp(key)
	
def maxKoord(axis, list):
	maxV= None
	if axis == 'x':
		for data in list:
			if(maxV is None or data[0] > maxV[0]):
				maxV = data
		return maxV
	elif axis == 'y':
		for data in list:
			if(maxV is None or data[1] > maxV[1]):
				maxV = data
		return maxV

def clickOnColor(target, color, toleranz, faktor, stop):
	targetColor = pyautogui.pixel(target)
	if np.allclose(targetColor, color, toleranz, faktor):
		click(target, stop)

def clickOffColor(target, color, toleranz, faktor, stop):
	targetColor = pyautogui.pixel(target)
	if np.allclose(targetColor, color, toleranz, faktor) == False:
		click(target, stop)
	
def clickOnPicture(path, toleranceX, toleranceY):
	target = pyautogui.locateOnScreen(path, grayscale=True, confidence=0.8)
	if target != None:
		location = [(target[0],target[0]+ toleranceX),(target[1],target[1]+toleranceY)]
		click(genTarget(location), 0.3)
		return True 
	else:
		return False

def picToCoordinates(loc, toleranceX, toleranceY):
	location = [(loc[0],loc[0]+ toleranceX),(loc[1],loc[1]+toleranceY)]
	return genTarget(location)

def ocr(target):   # traget is (left, top, width, height)
    img = pyautogui.screenshot(region=target)
    output = pytesseract.image_to_string(img)
    return output

def checkEnergiePS():
	data = ocr((485,40,80,40)).split('/')
	if int(data[0]) > 5:
		return int(data[0])
	else:
		return False
	
def genTarget(target):
	return  (random.randint(target[0][0],target[0][1]),random.randint(target[1][0], target[1][1]))

def locate(path):
	return pyautogui.locate(path,0.8)

def clickIfPicture(locat, target):
	if pyautogui.locateOnScreen(locat, grayscale=True, confidence=0.8) != None:
		time.sleep(np.random.uniform(1, 1.5))
		clickOnPicture(target, 20, 10)

def initFormBastion():
	## Genügend Energie ?
	if checkEnergiePS()>5:
	#Starte Schlacht
		click(genTarget(startFight),0.2)
		time.sleep(3)
	#Wähle Kampagne
		click(genTarget(kampagne),0.2)
		time.sleep(np.random.uniform(0.6, 2))
		clickOnPicture('kp3.png', 30, 20)
		time.sleep(np.random.uniform(0.6, 2))
	# Wähle Schlachtfeld
		rooms = list(locateAll('schlachtB.png', pyautogui.screenshot(), confidence=0.8))
		lastRoom = maxKoord('y',rooms)
		time.sleep(np.random.uniform(1, 3))
		click(picToCoordinates(lastRoom, 30, 10), 0.2)
		time.sleep(np.random.uniform(1, 3))
	#Starte Spiel
		clickOnPicture('Start.png', 70, 30)
		time.sleep(np.random.uniform(4, 10))
	else:
		print("to Low on Energie")



while keyboard.is_pressed('q') == False:
	if pyautogui.locateOnScreen('artefakt.png', confidence=0.8) != None:
		clickOnPicture('verbessern.png', 50, 20)
		time.sleep(np.random.uniform(0.5,0.6))
	if pyautogui.locateOnScreen('bastion.png', confidence=0.9) != None:
		initFormBastion()
	clickIfPicture('chapscip.png', 'chapscip.png')
	if pyautogui.locateOnScreen('Sieg.png', grayscale=True, confidence=0.8) != None:
		time.sleep(0.3)
		clickOnPicture('weiter blitz.png', 20, 10)
		time.sleep(np.random.uniform(1, 2))
		clickOnPicture('start.png',30, 25)
		time.sleep(np.random.uniform(0.2, 0.5))
	elif pyautogui.locateOnScreen('weiter.png', confidence=0.8) != None:
		clickOnPicture('weiter.png', 35, 10)
		time.sleep(np.random.uniform(0.2,0.4))
	elif pyautogui.locateOnScreen('cancel.png', grayscale=True, confidence=0.7):
		clickOnPicture('cancel.png', 20, 20)
	clickIfPicture('niederlage.png', 'replay.png')
	clickIfPicture('levelup.png','levelup.png')
	#clickIfPicture('cancelHero.png', 'cancelHero.png')
	time.sleep(np.random.uniform(1, 2))


	

    
	
