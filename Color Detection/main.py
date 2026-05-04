#Simple color detection system in real-time with only Python & OpenCV

import cv2
import numpy as np
from PIL import Image

def getLimits(color, range):
    c = np.uint8([[color]]) #creats 1x1 pixel image of color as unsigned 8-bit int
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = int(hsvC[0][0][0]) #grabs the pixel in the 1st row and col of the Hue channel
    
    lowerLimit = max(hue - range, 0), 100, 100 #100 ignores very dark shadows 
    upperLimit = min(hue + range, 179), 255, 255 #255 is max saturation and brightness

    #converts to format accepted by OpenCV
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit,upperLimit

cam = cv2.VideoCapture(0)
yellow = [0, 255, 255]

while True:
    ret, frame = cam.read()

    #color detection (via HSV hue channel)
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = getLimits(yellow, 5)
    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit) #finds location of pixels within interval of selected hue (section in the color circle)

    mask_ = Image.fromarray(mask) #converts format for pillow
    bbox = mask_.getbbox() #uses pillow to get bounding box
    # print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), [255, 0, 0], 3)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cam.release()
cv2.destroyAllWindows()
