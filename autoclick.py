import time
from mouse import clickBtn
from images import load_images

def minutes(seconds):
    return seconds*60

def main():
    
    targets = load_images(dir_path='targets/')
    last = {
        "simpleClick":0
    } 

    while True:
        now = time.time()
        if now - last["simpleClick"] > minutes(1):
            last["simpleClick"] = now
            clickBtn(targets['button'])
  
if __name__ == '__main__':
   
    main()
