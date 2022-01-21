import time
import pyautogui
from screen import positions

def clickBtn(img, timeout=3, threshold=0.7):
    #Search for img in the screen, if found moves the cursor over it and clicks.
    start = time.time()
    has_timed_out = False
    while(not has_timed_out):
        matches = positions(img, threshold=threshold)

        if(len(matches)==0):
            has_timed_out = time.time()-start > timeout
            continue

        x,y,w,h = matches[0]
        pos_click_x = x+w/2
        pos_click_y = y+h/2
        pyautogui.moveTo(pos_click_x,pos_click_y,1)
        pyautogui.click()
        return True

    return False