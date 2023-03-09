from findandclick import FindandClick
import time
import pyautogui as py

def Quest():
    if py.locateOnScreen(r"assets\Quest\Quest In.PNG", confidence=0.85):
        FindandClick.findandClick(r"assets\Quest\Quest In.PNG")
        time.sleep(0.9)
        FindandClick.findandClick(r"assets\Quest\Quest In2.PNG")
        time.sleep(0.9)


        if py.locateOnScreen(r"assets\Quest\mission1.PNG", confidence=0.75):
            FindandClick.findandClick(r"assets\Quest\mission1.PNG")
            time.sleep(0.9)
            for i in range(9):
                if (py.locateOnScreen(r"assets\Quest\Reading.PNG", confidence=0.75)
                or py.locateOnScreen(r"assets\Quest\exit.PNG", confidence=0.75)):
                    break
                FindandClick.findandClick(r"assets\Quest\auto.PNG")
                time.sleep(0.4)

                
        if py.locateOnScreen(r"assets\Quest\mission2.PNG", confidence=0.75):
            FindandClick.findandClick(r"assets\Quest\mission2.PNG")
            time.sleep(0.9)
            for i in range(9):
                if (py.locateOnScreen(r"assets\Quest\Reading.PNG", confidence=0.75)
                or py.locateOnScreen(r"assets\Quest\exit.PNG", confidence=0.75)):
                    break
                FindandClick.findandClick(r"assets\Quest\auto.PNG")
                time.sleep(0.4)

        if py.locateOnScreen(r"assets\Quest\Day mission.PNG", confidence=0.75):
            FindandClick.findandClick(r"assets\Quest\Day mission.PNG")
            time.sleep(0.9)
            
            for i in range(6):
                if py.locateOnScreen(r"assets\Quest\Day End.PNG", confidence=0.75):
                    break
                FindandClick.findandClick(r"assets\Quest\Day Geting.PNG")
                time.sleep(0.4)
                FindandClick.findandClick(r"assets\Quest\Day missin Box.PNG")
                time.sleep(0.4)
        FindandClick.findandClick(r"assets\Quest\teritory Purpose.PNG")
        time.sleep(0.9)

        for i in range(10):
            FindandClick.findandClick(r"assets\Quest\Day Geting.PNG")
            time.sleep(0.6)

        if py.locateOnScreen(r"assets\Quest\VIP.PNG", confidence=0.7):
            FindandClick.findandClick(r"assets\Quest\VIP.PNG")
            time.sleep(1.0)
            FindandClick.findandClick(r"assets\Quest\VIP Box.PNG")
            time.sleep(5.0)

        FindandClick.findandClick(r"assets\guild\X.PNG")
        time.sleep(0.9)