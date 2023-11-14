import pytesseract
import pyautogui, cv2

pytesseract.tesseract_cmd = r"path totesseract"


def ocr(region):
    
    img_screenshot = cv2.cvtColor(pyautogui.screenshot(region=region), cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_string(img_screenshot, lang='eng',config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789/:.')

    return data
