from findandclick import FindandClick
import time
import pyautogui as py

def Army():
    if py.locateOnScreen(r"assets\Product\Army.PNG", confidence=0.75):
        FindandClick.findandClick(r"assets\Product\Army.PNG")
        time.sleep(1.4)
        FindandClick.findandClick(r"assets\Product\siege weapon.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\Product\Traning.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(0.9)

def dimensionaldoor():
    py.moveTo(400, 300)
    py.dragTo(700, 300, 1)
    if py.locateOnScreen(r"assets\Product\Puple Door.PNG", confidence=0.75):
        FindandClick.findandClick(r"assets\Product\Puple Door.PNG")
        time.sleep(1.4)
        FindandClick.findandClick(r"assets\Product\Box.PNG")
        time.sleep(0.9)
        if py.locateOnScreen(r"assets\Product\Open.PNG", confidence=0.75):
            for i in range(3):
                FindandClick.findandClick(r"assets\Product\Open.PNG")
                time.sleep(0.9)
                py.click(300, 200)
                time.sleep(0.1)
                py.click(300, 200)
                time.sleep(0.1)
                py.click(300, 200)
                time.sleep(0.1)
                py.click(300, 200)
                time.sleep(0.1)
                py.click(300, 200)
                time.sleep(2.4)
                FindandClick.findandClick(r"assets\guild\X.PNG")
                time.sleep(1.4)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(0.9)
        # if py.locateOnScreen(r"assets\Product\All Card.PNG", confidence=0.7):
        #     FindandClick.findandClick(r"assets\Product\All Card.PNG")
        #     time.sleep(0.9)
        #     for i in range(10):
        #         py.scroll(100)
        #         FindandClick.findandClick(r"assets\Product\Target.PNG")
        #         time.sleep(0.9)
        #         FindandClick.findandClick(r"assets\Product\LevelUp.PNG")
        #         time.sleep(0.9)
        #         FindandClick.findandClick(r"assets\Product\X.PNG")
        #         time.sleep(0.9)
        #         FindandClick.findandClick(r"assets\guild\X.PNG")
        #         time.sleep(0.9)
        #     FindandClick.findandClick(r"assets\guild\X.PNG")
        #     time.sleep(0.9)
        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(0.9)

def Arena():
    py.moveTo(400, 300)
    py.dragTo(700, 300, 1)
    if (py.locateOnScreen(r"assets\Product\Arena.PNG", confidence=0.75)
        and py.locateOnScreen(r"assets\Product\ArenaTarget.PNG", confidence=0.5)) :
        FindandClick.findandClick(r"assets\Product\Arena.PNG")
        time.sleep(1.9)
        while True:
            FindandClick.findandClick(r"assets\Product\Challenge.PNG")
            time.sleep(0.9)
            FindandClick.findandClick(r"assets\Product\participation.PNG")
            time.sleep(80)
            FindandClick.findandClick(r"assets\Product\back.PNG")
            time.sleep(5)
            if py.locateOnScreen(r"assets\Product\05.PNG", confidence=0.9):
                break
    FindandClick.findandClick(r"assets\guild\X.PNG")
    time.sleep(0.9)

def ReSet():
    py.moveTo(700, 300)
    py.dragTo(400, 300, 1)
    py.moveTo(700, 300)
    py.dragTo(400, 300, 1)


