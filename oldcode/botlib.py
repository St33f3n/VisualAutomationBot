from PIL import Image
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random


def click(coordinates, stop):
    time.sleep(np.random.uniform(stop, 2 * stop))


def keyPress(key, stop):
    pyautogui.keyDown(key)
    time.sleep(np.random.uniform(stop, 2 * stop))
    pyautogui.keyUp(key)


def maxKoord(axis, list):
    maxV = None
    if axis == "x":
        for data in list:
            if maxV is None or data[0] > maxV[0]:
                maxV = data
        return maxV
    elif axis == "y":
        for data in list:
            if maxV is None or data[1] > maxV[1]:
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
        location = [
            (target[0], target[0] + toleranceX),
            (target[1], target[1] + toleranceY),
        ]
        click(genTarget(location), 0.3)
        return True
    else:
        return False


def picToCoordinates(loc, toleranceX, toleranceY):
    location = [(loc[0], loc[0] + toleranceX), (loc[1], loc[1] + toleranceY)]
    return genTarget(location)


def ocr(target):  # traget is (left, top, width, height)
    img = pyautogui.screenshot(region=target)
    return output


def genTarget(target):
    return (
        random.randint(target[0][0], target[0][1]),
        random.randint(target[1][0], target[1][1]),
    )


def locate(path):
    return pyautogui.locate(path, 0.8)


def clickIfPicture(locat, target):
    if pyautogui.locateOnScreen(locat, grayscale=True, confidence=0.8) is not None:
        time.sleep(np.random.uniform(1, 1.5))
        clickOnPicture(target, 20, 10)
