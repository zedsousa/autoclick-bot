import time
import yaml
import pyautogui
from mouse import clickBtn
from images import load_images
from screen import positions

targets = load_images(dir_path='targets/')
stream = open("config.yaml", 'r')
c = yaml.safe_load(stream)


def rentHorse():
    time.sleep(10)
    horseNumber = c['horse_number']
    while True:
        pyautogui.hotkey('ctrl','t')
        url = 'https://play.pegaxy.io/renting/listing/'+str(horseNumber)
        pyautogui.write(url)    
        pyautogui.hotkey('enter')
        time.sleep(5)
        if(len(positions(targets['with-horse']))==0):
            start = time.time()
            while True:
                pyautogui.hotkey('f5')
                time.sleep(2)
                now = time.time()
                if (now - start > c['time_out']):
                    break

                if(len(positions(targets['with-horse']))>0):
                
                    if(clickBtn(targets['first-rent'])):
                        while True:
                            if(clickBtn(targets['captcha'])):
                                break

                        pyautogui.moveTo(c['rent_x'],c['rent_y'],1)
                        pyautogui.click()    
                        
                        while True:
                            if(clickBtn(targets['desaprovado'])):
                                break
                        while True:
                            if(clickBtn(targets['confirmar'])):
                                break 
                        while True:
                            if(clickBtn(targets['atividade'])):
                                break
                        time.sleep(5)    
                        pyautogui.moveTo(c['close_x'],c['close_y'],1)
                        pyautogui.click()    
                    break
                
        pyautogui.hotkey('ctrl','w')
        horseNumber+=10

def main():

    last = {
        "simpleClick":0
    } 

    while True:
        now = time.time()
        if now - last["simpleClick"] > 1:
            last["simpleClick"] = now
            rentHorse()
  
if __name__ == '__main__':
   
    main()
