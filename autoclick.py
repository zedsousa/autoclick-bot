import time
import sys
import pyautogui
from images import load_images
import telegram_send
from mouse import clickBtn
from images import load_images

images = load_images()

last_log_is_progress = False
COLOR = {
    'blue': '\033[94m',
    'default': '\033[99m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m'
}

def dateFormatted(format = '%Y-%m-%d %H:%M:%S'):
    datetime = time.localtime()
    formatted = time.strftime(format, datetime)
    return formatted

def minutes(seconds):
    return seconds*60

def logger(message, progress_indicator = False, color = 'default'):
    global last_log_is_progress
    color_formatted = COLOR.get(color.lower(), COLOR['default'])

    formatted_datetime = dateFormatted()
    formatted_message = "[{}] => {}".format(formatted_datetime, message)
    formatted_message_colored  = color_formatted + formatted_message + '\033[0m'

    
    # Start progress indicator and append dots to in subsequent progress calls
    if progress_indicator:
        if not last_log_is_progress:
            last_log_is_progress = True
            formatted_message = color_formatted + "[{}] => {}".format(formatted_datetime, '⬆️ Processing last action..')
            sys.stdout.write(formatted_message)
            sys.stdout.flush()
        else:
            sys.stdout.write(color_formatted + '.')
            sys.stdout.flush()
        return

    if last_log_is_progress:
        sys.stdout.write('\n')
        sys.stdout.flush()
        last_log_is_progress = False    

    print(formatted_message_colored)

    

    return True    

def sendMapImageToTelegram():
    if clickBtn(images['dead']):
        logger('📸 Taking a screenshot of the game')  
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'map_image.png')
        map_image = open('map_image.png', 'rb')

        logger('🗺️ Sending game image to telegram: ')
        telegram_send.send(images=[map_image])    

def main():
    
    targets = load_images(dir_path='targets/')
    last = {
        "simpleClick":0
    } 

    while True:
        now = time.time()
        if now - last["simpleClick"] > 60:
            last["simpleClick"] = now
            
            sendMapImageToTelegram()
  
if __name__ == '__main__':
   
    main()
