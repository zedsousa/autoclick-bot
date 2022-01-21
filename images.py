from os import listdir
from cv2 import cv2

def remove_suffix(input_string, suffix):
    #Returns the input_string without the suffix
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

def load_images(dir_path='./targets/'):
    #Loads all images from the targets folder, removes the .png suffix and returns a list of the loaded images
    file_names = listdir('./'+dir_path)
    targets = {}
    for file in file_names:
        path = dir_path + file
        targets[remove_suffix(file, '.png')] = cv2.imread(path)

    return targets