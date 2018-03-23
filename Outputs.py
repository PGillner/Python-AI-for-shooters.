import pyautogui as pag
import win32gui as wgui
import sys

byX = 0
byY = 0

pag.FAILSAFE = False

##  State max 2, MouseLClick max 1, MouseRClick max 1, Keys max 9.
output = [0, 0, 0 ,0]

def MouseMove(byY, byX):
    byY = byY * -1
    pag.moveRel(byX, byY)

def MouseLClick(State):
    if State == "Down":
        pag.mouseDown(button = "left")
        output[0] = 0
        output[1] = 1
    elif State == "Up":
        pag.mouseUp(button = "left")
        output[0] = 1
        output[1] = 1
    elif State == "None":
        output[0] = 2
        output[1] = 1

def MouseRClick(State):
    if State == "Down":
        pag.mouseDown(button = "right")
        output[0] = 0
        output[2] = 1
    elif State == "Up":
        pag.mouseUp(button = "right")
        output[0] = 1
        output[2] = 1
    elif State == "None":
        output[0] = 2
        output[2] = 1

def Keys(key, State):
    # A
    if key == "a" and State == "Down":
        pag.keyDown(key)
        output[0] = 0
        output[3] = 0
    elif key == "a" and State == "Up":
        pag.keyUp(key)
        output[0] = 1
        output[3] = 0
    elif key == "a" and State == "None":
        output[0] = 2
        output[3] = 0

    # W
    elif key == "w" and State == "Down":
        pag.keyDown(key)
        output[0] = 0
        output[3] = 1
    elif key == "w" and State == "Up":
        pag.keyUp(key)
        output[0] = 1
        output[3] = 1
    elif key == "w" and State == "None":
        output[0] = 2
        output[3] = 1

    # S
    elif key == "s" and State == "Down":
        pag.keyDown(key)
        output[0] = 0
        output[3] = 2
    elif key == "s" and State == "Up":
        pag.keyUp(key)
        output[0] = 1
        output[3] = 2
    elif key == "s" and State == "None":
        output[0] = 2
        output[3] = 2

    # D
    elif key == "d" and State == "Down":
        pag.keyDown(key)
        output[0] = 0
        output[3] = 3
    elif key == "d" and State == "Up":
        pag.keyUp(key)
        output[0] = 1
        output[3] = 3
    elif key == "d" and State == "None":
        output[0] = 2
        output[3] = 3

    # Ctrl
    elif key == "ctrl" and State == "Down":
        pag.keyDown(key)
        output[0] = 0
        output[3] = 4
    elif key == "ctrl" and State == "Up":
        pag.keyUp(key)
        output[0] = 1
        output[3] = 4
    elif key == "ctrl" and State == "None":
        output[0] = 2
        output[3] = 4

    # Alt
    elif key == "alt" and State == "None":
        pag.press(key)
        output[0] = 2
        output[3] = 5

    # Shift
    elif key == "shift" and State == "Down":
        pag.keyDown(key)
        output[0] = 0
        output[3] = 6
    elif key == "shift" and State == "Up":
        pag.keyUp(key)
        output[0] = 1
        output[3] = 6
    elif key == "shift" and State == "None":
        output[0] = 2
        output[3] = 6

    # Space
    elif key == "space" and State == "None":
        pag.press(key)
        output[0] = 2
        output[3] = 7

    # 1
    elif key == "1" and State == "None":
        pag.press(key)
        output[0] = 2
        output[3] = 8

    # 2
    elif key == "2" and State == "None":
        pag.press(key)
        output[0] = 2
        output[3] = 9

    else:

def keys_being_output(output):
    outputlist = output
    return outputlist
        
        


