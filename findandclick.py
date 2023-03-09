import pyautogui as py

class FindandClick:
    def findandClick(png):
        Po = py.locateOnScreen(png, confidence=0.75)
        if(Po):
            py.click(Po)

def Scroll(PM):
    py.scroll(PM)

#그냥 숫자넣자
# py.moveTo(400, 300)
# py.dragTo(700, 300, 1)