
# from types import prepare_class
# import numpy as np
# from glob import glob
# import torch
import os
from PIL import Image

COL = 8 # number of columns in the image
ROW = 9 # number of raws in the image
UNIT_HEIGHT_SIZE = 2048 #the height of the patch
UNIT_WIDTH_SIZE = 2048 #the width of the patch
SAVE_QUALITY = 100 
def concat_images(image_names,savePath,name):
    image_files = []
    for i in range(len(image_names)):
        image_files.append(Image.open(image_names[i]))

    target = Image.new('RGB', (UNIT_WIDTH_SIZE * COL, UNIT_HEIGHT_SIZE * ROW)) 

    for row in range(ROW):
        for col in range(COL):    
            target.paste(image_files[COL*row+col], (0 + UNIT_WIDTH_SIZE*col, 0 + UNIT_HEIGHT_SIZE*row))
    target.save(savePath+'\\' + name + '.jpg', quality=SAVE_QUALITY) 


if __name__ == "__main__":

    path = '18_fake_cd8' # patches folder
    savePath = 'outputwsi' # wsi will be saved in this folder
    name = '18_fake_cd8' # wsi saved name
    
    files=os.listdir(path)
    hfile = []
    hfile1 = []
    hfile2 = []

    for i in files:
        img_path = os.path.join(path,i)
        if(img_path[13:15][1]=='_'):
            hfile1.append(img_path)
        else:
            hfile2.append(img_path)
    hfile = hfile1 + hfile2

    if not os.path.exists(savePath):  
        os.makedirs(savePath)    
    
    concat_images(hfile,savePath,name)
