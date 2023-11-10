import pytesseract
import pyautogui

pytesseract.tesseract_cmd = r"path totesseract"


def ocr(coordinates):
    area = pyautogui.screenshot(region=coordinates)
    data_string = pytesseract.image_to_string(area)
    return data_string
