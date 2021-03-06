#todo mirroring with average laplacian and sobel median and gaussian

import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
from skimage.color import rgb2gray
sujihye = cv2.imread('./goddess2.jpg')

b, g, r = cv2.split(sujihye)
original = cv2.merge([r,g,b])

gray_original = rgb2gray(original)

skimage.io.imshow(original)

#only 3x3 5x5 7x7 ......
def makeLaplacian_filter(w,h):
    res = np.zeros((w,h))
    center_x = w//2
    center_y = h//2
    res[center_x][center_y]= 2**(w-1)
    center_val = res[center_x][center_y]
   # print(center_val,div_val,w_i)
    ypm=1
    xpm=1
    div_val=2
    res[center_x-xpm][center_y] = center_val/np.sqrt(center_val)
    res[center_x][center_y-ypm] = center_val/np.sqrt(center_val)
    res[center_x+xpm][center_y] = center_val/np.sqrt(center_val)
    res[center_x][center_y+ypm] = center_val/np.sqrt(center_val)
    center_val = res[center_x][center_y+ypm]
    center_val = res[center_x-xpm][center_y]/div_val
    xpm+=1
    ypm+=1
    while((center_x+xpm)<w):
        res[center_x-xpm][center_y] = center_val
        res[center_x][center_y-ypm] = center_val
        res[center_x+xpm][center_y] = center_val
        res[center_x][center_y+ypm] = center_val
        xpm+=1
        ypm+=1
        center_val = res[center_x-xpm][center_y]/div_val
    res[center_x-xpm+1][center_y] = 1
    res[center_x][center_y-ypm+1] = 1
    res[center_x+xpm-1][center_y] = 1
    res[center_x][center_y+ypm-1] = 1
    res[center_x][center_y]*=-1
    return res

#only 3x3 5x5 7x7 ......
def average_filter(w,h):
    res = np.ones((w,h))
    res /=(w*h)
    return res

def mirror_padding(w,h,img):
    ori_x_max = img.shape[0]
    ori_y_max = img.shape[1]
    ori_chennal = img.shape[2]
    padding_x_size = np.int((w-1)/2)
    padding_y_size = np.int((h-1)/2)
    res = np.zeros((ori_x_max+padding_x_size*2,ori_y_max+padding_y_size*2,ori_chennal))
    res[padding_x_size:ori_x_max+padding_x_size,padding_y_size:ori_y_max+padding_y_size:,] = img
    res[padding_x_size-1::-1,padding_y_size:padding_y_size+ori_y_max:,] = img[0:padding_x_size,0:ori_y_max]
    res[ori_x_max+padding_x_size:ori_x_max+padding_x_size*2,padding_y_size:padding_y_size+ori_y_max:,] = img[ori_x_max-1:ori_x_max-padding_x_size-1:-1,0:ori_y_max]
    res[padding_x_size-1::-1,padding_y_size:padding_y_size+ori_y_max:,] = img[0:padding_x_size,0:ori_y_max]
    res[0:ori_x_max+2*padding_x_size, padding_y_size:0:-1,] = res[0:ori_x_max+2*padding_x_size, padding_y_size:padding_y_size*2:,]
    res[0:ori_x_max+2*padding_x_size, ori_y_max+padding_y_size:ori_y_max+padding_y_size*2] = res[0:ori_x_max+2*padding_x_size,ori_y_max+padding_y_size-1:ori_y_max-1:-1,]
    return res

def laplcian_adaption(w,h,img):
    res =  np.zeros(img.shape)
    mirror_img = mirror_padding(w,h,img)
    laplacian_filter =  makeLaplacian_filter(w,h)
    for x in range(0,img.shape[0]):
        for y in range(0,img.shape[1]):
            res[x,y,0] = np.mean(np.dot(laplacian_filter,mirror_img[x:x+w,y:y+h,0]))
            res[x,y,1] = np.mean(np.dot(laplacian_filter,mirror_img[x:x+w,y:y+h,1]))
            res[x,y,2] = np.mean(np.dot(laplacian_filter,mirror_img[x:x+w,y:y+h,2]))
    return res
    
def average_adaption(w,h,img):
    res =  np.zeros(img.shape)
    mirror_img = mirror_padding(w,h,img)
    avg_filter =  average_filter(w,h)
    for x in range(0,img.shape[0]):
        for y in range(0,img.shape[1]):
            res[x,y,0] = np.sum(np.dot(avg_filter,mirror_img[x:x+w,y:y+h,0]))
            res[x,y,1] = np.sum(np.dot(avg_filter,mirror_img[x:x+w,y:y+h,1]))
            res[x,y,2] = np.sum(np.dot(avg_filter,mirror_img[x:x+w,y:y+h,2]))
    return res