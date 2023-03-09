from window import Window
from findandclick import Scroll
import time
from Guild import GuildGet
from GreenBox import GreenBoxGet
from Quest import Quest
from Resource import Resource
from Product import *

Window()
time.sleep(0.1)

while True:
    GreenBoxGet()
    time.sleep(0.1)
    GuildGet()
    time.sleep(0.1)
    GreenBoxGet()
    time.sleep(0.1)
    Quest()
    time.sleep(0.1)
    Army()
    time.sleep(0.1)
    GreenBoxGet()
    time.sleep(0.1)
    dimensionaldoor()
    time.sleep(0.1)
    Arena()
    ReSet()
    Resource()

    # if LOC(r"auto\python\mobile BlueStacks\WannaI\Green.PNG"):
    #     print("error")
    #     break



