import torch.nn as nn
import torchvision.transforms as transforms
import os
import cv2
if __name__ =="__main__":
    transf = transforms.ToTensor()
    loss = nn.MSELoss(reduction='mean')
    "change the folder can get different wsi result"
    path_real = '19_real'
    path_fake = '19_fake'

    files = os.listdir(path_real)
    acc= 0

    for file in files:

        img_real = os.path.join(path_real,file)
        img_fake = os.path.join(path_fake,file)

        original = cv2.imread(img_real)
        contrast = cv2.imread(img_fake)

        input = transf(original)
        target = transf(contrast)
        
        Loss = loss(input,target)
        acc += Loss

    # print(acc)
    print(acc/len(files))

# 18 tensor(0.0129)
# 19 tensor(0.0105)
