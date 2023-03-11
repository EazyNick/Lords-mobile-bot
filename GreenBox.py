from findandclick import FindandClick
import time
import pyautogui as py

def GreenBoxGet():
    if py.locateOnScreen(r"assets\Green Present Box\Light Green Box.PNG", confidence=0.75):
        FindandClick.findandClick(r"assets\Green Present Box\Light Green Box.PNG")
        time.sleep(1.4)
        FindandClick.findandClick(r"assets\Green Present Box\Get2.PNG")
        time.sleep(1.4)
        FindandClick.findandClick(r"assets\Green Present Box\Get.PNG")
        time.sleep(1.9)