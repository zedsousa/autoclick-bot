import time
from mouse import clickBtn
import pyautogui
from images import load_images
from screen import positions

targets = load_images(dir_path='targets/')
def minutes(seconds):
    return seconds*60

def raceHorse():
    time.sleep(10)
    while True:
        while True:
            if(clickBtn(targets['start'])):
                break
        while True:
            if(clickBtn(targets['solicitacao'])):
                break
        while True:
            if(clickBtn(targets['assinar'])):
                break
        time.sleep(5)    
        while True:
            if(clickBtn(targets['atividade'])):
                break    
        time.sleep(80)    
        pyautogui.moveTo(372,620,1)
        pyautogui.click() 



def rentHorse():
    time.sleep(10)
    horseNumber = 1688601
    while True:
        pyautogui.hotkey('ctrl','t')
        url = 'https://play.pegaxy.io/renting/listing/'+str(horseNumber)
        pyautogui.write(url)    
        pyautogui.hotkey('enter')
        time.sleep(5)
        if(len(positions(targets['with-horse']))==0):
            while True:
                pyautogui.hotkey('f5')
                time.sleep(2)

                if(len(positions(targets['with-horse']))>0):
                    if(len(positions(targets['10%']))>0):
                        if(clickBtn(targets['first-rent'])):
                            while True:
                                if(clickBtn(targets['captcha'])):
                                    break

                            pyautogui.moveTo(440,471,1)
                            pyautogui.click()    
                            
                            while True:
                                if(clickBtn(targets['desaprovado'])):
                                    break
                            while True:
                                if(clickBtn(targets['confirmar'])):
                                    break
                            time.sleep(5)  
                            pyautogui.moveTo(480,454,1)
                            pyautogui.click()  
                            while True:
                                if(clickBtn(targets['atividade'])):
                                    break
                            time.sleep(5)    
                            pyautogui.moveTo(581,295,1)
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
