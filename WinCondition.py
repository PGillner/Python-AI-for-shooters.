import pytesseract
import cv2
import random

def WinChecker(folder, screen):
    img = cv2.imread(r"F:\IronSight_AI\Images\{}\Screen{}.jpg".format(folder, ScreenCount), 0)
    text = pytesseract.image_to_string(img, lang = "eng")
    if text == "Victory!":
        State = "Victory"
        return State
    elif text == "Defeat":
        State = "Defeat"
        return State
    else:
        State = "None Detected"
        return State
