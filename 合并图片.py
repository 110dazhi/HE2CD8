# 18_0_0 -18_0_7
# 18_8_0 - 18_8_7
from types import prepare_class
import numpy as np
from glob import glob
import torch
import os
from PIL import Image

COL = 8 #指定拼接图片的列数
ROW = 8 #指定拼接图片的行数
UNIT_HEIGHT_SIZE = 256 #图片高度
UNIT_WIDTH_SIZE = 256 #图片宽度
SAVE_QUALITY = 100 #保存的图片的质量 可选0-100
def concat_images(image_names, name, savePath):
    image_files = []
    for i in range(COL):
        for j in range(ROW):

            image_files.append(Image.open(image_names[i][j]))

    target = Image.new('RGB', (UNIT_WIDTH_SIZE * COL, UNIT_HEIGHT_SIZE * ROW)) #创建成品图的画布
    #第一个参数RGB表示创建RGB彩色图，第二个参数传入元组指定图片大小，第三个参数可指定颜色，默认为黑色
    for row in range(ROW):
        for col in range(COL):

            target.paste(image_files[COL*row+col], (0 + UNIT_WIDTH_SIZE*col, 0 + UNIT_HEIGHT_SIZE*row))
    target.save(savePath+'\\' + name + '.jpg', quality=SAVE_QUALITY) #成品图保存


files=np.loadtxt('E:\\HECD8\\testlist.txt',dtype=str)



for i in files:
    tensorsum = torch.tensor([])
    hfile = []
    if i.split('_')[0] != '18':
        continue
    for k in range(8):
        sig = i +'_' + str(k) 
        # path = 'fake18\\%s_%s_*.pt'%(str(i),k)
        # print(sig)
        hfile.append(glob(sig+'*'))
    # print(hfile)
    # print(hfile)

    savePath = 'output'
    concat_images(hfile,i,savePath)
