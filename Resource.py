from findandclick import FindandClick
import time
import pyautogui as py
from window import Window

def Resource():
    if not py.locateOnScreen(r"assets\Resource\Start Signal.PNG", confidence=0.9):
        FindandClick.findandClick(r"assets\Resource\Map.PNG")
        time.sleep(1.4)
        
        while True:
            if (py.locateOnScreen(r"assets\Resource\End.PNG", confidence=0.75)
            or py.locateOnScreen(r"assets\Resource\NoTroops.PNG", confidence=0.75)):
                FindandClick.findandClick(r"assets\Resource\Okay.PNG")
                time.sleep(1.4)
                break
            
            py.moveTo(500, 250)
            py.scroll(-100)
            if (py.locateOnScreen(r"assets\Resource\Food.PNG", confidence=0.5)
            or py.locateOnScreen(r"assets\Resource\Resource3.PNG", confidence=0.5)
            or py.locateOnScreen(r"assets\Resource\Rock.PNG", confidence=0.5)
            or py.locateOnScreen(r"assets\Resource\Wood.PNG", confidence=0.5)
            or py.locateOnScreen(r"assets\Resource\Wood2.PNG", confidence=0.5)):
                FindandClick.findandClick(r"assets\Resource\Food.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\Resource3.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\Rock.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\Wood.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\Wood2.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\collection.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\Choice.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Resource\participation.PNG")
                time.sleep(0.4)
        FindandClick.findandClick(r"assets\Resource\Home.PNG")
        time.sleep(0.4)

def Resource2():
    FindandClick.findandClick(r"assets\Resource\Map.PNG")
    time.sleep(1.4)
        
    while True:
        if py.locateOnScreen(r"assets\Resource\End.PNG", confidence=0.75):
            FindandClick.findandClick(r"assets\Resource\Okay.PNG")
            time.sleep(1.4)
            break

        py.moveTo(500, 250)
        py.scroll(-100)
        if (py.locateOnScreen(r"assets\Resource\Food.PNG", confidence=0.5)
        or py.locateOnScreen(r"assets\Resource\Resource3.PNG", confidence=0.5)
        or py.locateOnScreen(r"assets\Resource\Rock.PNG", confidence=0.5)
        or py.locateOnScreen(r"assets\Resource\Wood.PNG", confidence=0.5)
        or py.locateOnScreen(r"assets\Resource\Wood2.PNG", confidence=0.5)):
            FindandClick.findandClick(r"assets\Resource\Food.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\Resource3.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\Rock.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\Wood.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\Wood2.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\collection.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\Choice.PNG")
            time.sleep(0.4)
            FindandClick.findandClick(r"assets\Resource\participation.PNG")
            time.sleep(0.4)
    FindandClick.findandClick(r"assets\Resource\Home.PNG")
    time.sleep(0.4)

# Window()
# time.sleep(0.2)
# Resource2()




