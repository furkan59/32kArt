
from PIL import Image 
import numpy as np
import cv2 
import math 
import random


def fractal5(power):
    height = 500
    width = 500
    image = np.zeros((height,width,3), np.uint8)

    b = 0
    g = 0
    r = 0
    for x in range(width): 
        for y in range(height):
            constant = 1
            b = (((x**2) + (y**2))**power)*constant % 255
            g = (((x**2)+ (y**2))**power)*constant % 255
            r = (((x**2)+ (y**2))**power)*constant % 255
            image[y,x,0] = b
            image[y,x,1] = g
            image[y,x,2] = r

    return image

def show(image,name="image"):
    cv2.imshow(name, image) 
    
    

if __name__ == "__main__": 
  
    image = fractal5(11)
    show(image,"11")

    image = fractal5(13)
    show(image,"13")

    image = fractal5(15)
    show(image,"15")

    cv2.waitKey(0)  
  
    cv2.destroyAllWindows()  
