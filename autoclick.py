import time
import pyautogui
import pandas as pd
from logger import logger
from mouse import clickBtn
from images import load_images
from screen import positions
from datetime import datetime

targets = load_images(dir_path='targets/')

def minutes(seconds):
    return seconds*60

def checkHungry():
    logger('🍴 Check for hungry workers')

    chicken_icon = positions(targets['chicken-icon'])
    if(len(chicken_icon)>0):
        print(len(chicken_icon), "worker(s) hungry!")
        giveChicken()

def giveChicken():
    logger('🍗 Giving chicken to worker')

    clickBtn(targets['chicken-icon'])
    time.sleep(3)
    if(clickBtn(targets['give-chicken'])):
        food_record = {'date': str(datetime.now()), 'value': "alimentou um trabalhador"}
        
    else:   
        food_record = {'date': str(datetime.now()), 'value': "não encontrou o botão give chicken"}

    food_database = pd.read_csv('database.csv')
    food_database = food_database.append(food_record, ignore_index=True)
    food_database.to_csv('database.csv', index=False)

def backHome():
    finished_icon = positions(targets['finished-working'])

    if(len(finished_icon)>0):
        logger("⚒️ Um trabalhador terminou o trabalho")

        if(clickBtn(targets['finished-working'])):
            clickBtn(targets['call-back-home'])  
            goToTown()
            time.sleep(1)
            clickBtn(targets['house'])

            if(len(positions(targets['regular-bed-avaliable']))==0):
                buyBed()    
            
            restWorker()

def buyBed():
    clickBtn(targets['empty'])
    time.sleep(1)
    clickBtn(targets['regular-bed'])

def restWorker():
    clickBtn(targets['regular-bed-avaliable'])
    clickBtn(targets['jacinto-becker'])#TODO trocar o print para a raridade, ou deixar uma posição fixa da tela
    clickBtn(targets['close-bed'])
    closeTown()

def goToTown():
    pyautogui.hotkey('ctrl','t')
    time.sleep(1)
    pyautogui.write('https://dev-alpha.worker.town/town')

def closeTown():
    pyautogui.hotkey('ctrl','w')

def main():
    
    
    last = {
        "check_hungry":0
    } 

    while True:
        now = time.time()
        if now - last["check_hungry"] > minutes(5):
            last["check_hungry"] = now
            goToTown()
            closeTown()
            checkHungry()
            
if __name__ == '__main__':
   
    main()
