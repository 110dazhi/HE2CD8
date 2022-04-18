import numpy as np
# from numpy.lib.function_base import blackman
# from numpy.lib.npyio import save
from skimage import io
from skimage.color import rgb2lab, deltaE_cie76
import os

def InitCanvas(width, height, color=(255, 255, 255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(str(contents))
    fh.close()

def caculate(imgpath,tcell_mask_path,tissue_mask_path):
    files = os.listdir(imgpath)
    files = sorted(files)
    
    i = 0
    acc_arr = {}
    for file in files:
        i=i+1
        
        path = os.path.join(imgpath,file)
        rgb = io.imread(path)
        # rgb = rgba2rgb(rgb)
        lab = rgb2lab(rgb)
        name = file.split('.')[0]+'.png'
        print(name)
        canvas = InitCanvas(rgb.shape[1],rgb.shape[0])
        canvas_tcell = InitCanvas(rgb.shape[1],rgb.shape[0])


        brown = [113,79,77]
        black = [0,0,0]
        threshold_brown = 25
        brown_3d = np.uint8(np.asarray([[brown]]))
        dE_brown = deltaE_cie76(np.squeeze(rgb2lab(brown_3d)), np.squeeze(lab))
        matrix = dE_brown < threshold_brown
        num1 = np.where(matrix==True)

        canvas_tcell[dE_brown < threshold_brown] = black
        save_tcell_mask_path = os.path.join(tcell_mask_path,name)
        io.imsave(save_tcell_mask_path,canvas_tcell)

        white = [255,255,255]
        threshold_white = 10
        white_3d = np.uint8(np.asarray([[white]]))
        dE_white = deltaE_cie76(np.squeeze(rgb2lab(white_3d)), np.squeeze(lab))
        matrix2 = dE_white > threshold_white
        num2 = np.where(matrix2==True)

        if len(num2[0]) == 0:
            acc = 0
        else:
            acc = len(num1[0])/len(num2[0])

        canvas[dE_white > threshold_white] = black


        
        acc_arr[file.split('.')[0]] = acc 
        
 
        
        save_tissue_mask_path = os.path.join(tissue_mask_path,name)
        io.imsave(save_tissue_mask_path,canvas)


    sorted (acc_arr)
    return acc_arr
if __name__=="__main__":  
    # wsi pstches folder
    img_folder_path='D:\\fake19_2048'
    
    # This txt file stores the file name of the patch and the corresponding distribution
    txt_path = "Dis_caculate_result\\19faketcellout\\19faketcellout.txt"
    # This folder stores the mask generated by the color segmentation of the t cell
    tcell_mask_path = "Dis_caculate_result\\19faketcellout\\tcell_mask"
    # This folder stores the mask generated by the color segmentation of the patch tissue
    tissue_mask_path = "Dis_caculate_result\\19faketcellout\\tissue_mask"

    if not os.path.exists(tcell_mask_path):  
        os.makedirs(tcell_mask_path)
    if not os.path.exists(tissue_mask_path):  
        os.makedirs(tissue_mask_path)    
    os.makedirs(os.path.dirname(txt_path), exist_ok=True)
    acc_arr = caculate(img_folder_path,tcell_mask_path,tissue_mask_path)

    filename = open(txt_path,'w')
    for k,v in acc_arr.items():
        filename.write(str(k)+':'+str(v))
        filename.write('\n')
    filename.close()



