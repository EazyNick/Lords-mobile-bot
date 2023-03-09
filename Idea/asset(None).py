from adb import adb_connect
import cv2, time
import numpy as np

device, client = adb_connect()

PresentBox = [87, 60, 14]

def take_screenshot():
    img_byte = device.screencap()
    img = cv2.imdecode(np.frombuffer(img_byte, np.uint8), flags=-1) # with alpha channel
    img = img[:, :, :3] # drop alpha channel
    return img

img = take_screenshot()

def Click(Img):

    for y in range(800,1000):
        for x in range(800, 1000):
            pixel = img[x, y]

            if np.array_equal(pixel, Img):
                print("발견")
                tap_x = x
                tap_y = y
                print('TAP (%d, %d)' % (tap_x, tap_y))
                device.input_swipe(tap_x, tap_y, tap_x, tap_y, 100)
                
            else:
                print("없는데?")
            


Click(PresentBox)