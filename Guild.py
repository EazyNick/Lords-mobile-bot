from findandclick import FindandClick
import time
import pyautogui as py

def GuildGet():
    if (py.locateOnScreen(r"assets\guild\hand.PNG", confidence=0.4)
    or py.locateOnScreen(r"assets\guild\3x hand.PNG", confidence=0.4)):
        FindandClick.findandClick(r"assets\guild\hand.PNG")
        time.sleep(1.4)
        FindandClick.findandClick(r"assets\guild\3x hand.PNG")
        time.sleep(1.4)
        FindandClick.findandClick(r"assets\guild\OkAY.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(1.4)

    if py.locateOnScreen(r"assets\guild\Present.PNG", confidence=0.85):
        FindandClick.findandClick(r"assets\guild\Message.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(1.1)
        FindandClick.findandClick(r"assets\guild\Present.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\In.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\Present Level.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\Allience Present.PNG")
        time.sleep(0.9)

        while True:
            for i in range(4):
                FindandClick.findandClick(r"assets\guild\Open.PNG")
                time.sleep(0.6)
            FindandClick.findandClick(r"assets\guild\Delete.PNG")
            if py.locateOnScreen(r"assets\guild\No present.PNG", confidence=0.75):
                break
            if py.locateOnScreen(r"assets\Exit.PNG", confidence=0.9):
                break
        time.sleep(0.5)
        FindandClick.findandClick(r"assets\guild\Bonus Box.PNG")
        time.sleep(0.9)

        while True:
            for i in range(5):
                FindandClick.findandClick(r"assets\guild\Open.PNG")
                time.sleep(0.6)
            FindandClick.findandClick(r"assets\guild\Delete.PNG")
            if py.locateOnScreen(r"assets\guild\No Bonus Present.PNG", confidence=0.75):
                break
            if py.locateOnScreen(r"assets\Exit.PNG", confidence=0.9):
                break
        time.sleep(0.5)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(0.9)