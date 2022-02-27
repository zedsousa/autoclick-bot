import mss
import numpy as np
from cv2 import cv2

def screenShot(monitor_number):
    #Get a screenshot of a monitor
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_number-1]
        sct_img = np.array(sct.grab(monitor))
        
        return sct_img[:,:,:3]

def positions(target, threshold=0.7,img = None):
    #Returns a list of positions of a target within an image
    if img is None:
        img = screenShot(1)

    result = cv2.matchTemplate(img,target,cv2.TM_CCOEFF_NORMED)
    h = target.shape[0]
    w = target.shape[1]

    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles
