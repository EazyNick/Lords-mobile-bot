from ppadb.client import Client
import cv2, time
import numpy as np
import time

def adb_connect(): #함수하나 만듬
    client = Client(host='127.0.0.1',port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print("No devices")
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스{device}')

    return device, client

device, client = adb_connect()

def findColor():
    img_byte = device.screencap() #byte형태의 이미지가 반환댐.
    img = cv2.imdecode(np.frombuffer(img_byte, np.uint8), flags=-1) #바이트의 이미지를 넘파이어레이 형태로 바꿔줌.
    img = img[:, :, :3]

    img = cv2.resize(img, dsize=None, fx=0.4, fy=0.4) #크기 줄여줌

    cv2.imshow('img', img) #윈도우로 띄우기
    cv2.imwrite('img.png', img)
    if cv2.waitKey(0) == ord('q'):
        exit()

findColor()