# Python code for Julia Fractal 
from PIL import Image 
import numpy as np
import cv2 
import math 
import random

# driver function 

def juliaFractal():
    # setting the width, height and zoom  
    # of the image to be created 
    #w, h, zoom = 1920,1080,1
    w, h, zoom = 640,480,1
    # creating the new image in RGB mode 
    bitmap = Image.new("RGB", (w, h), "white") 
  
    # Allocating the storage for the image and 
    # loading the pixel data. 
    pix = bitmap.load() 
     
    # setting up the variables according to  
    # the equation to  create the fractal 
    cX, cY = -0.7, 0.27015
    moveX, moveY = 0.0, 0.0
    maxIter = 255
   
    for x in range(w): 
        for y in range(h): 
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY 
            i = maxIter 
            while zx*zx + zy*zy < 4 and i > 1: 
                tmp = zx*zx - zy*zy + cX 
                zy,zx = 2.0*zx*zy + cY, tmp 
                i -= 1
  
            # convert byte to RGB (3 bytes), kinda  
            # magic to get nice colors 
            pix[x,y] = (i << 21) + (i << 10) + i*8
  
    # to display the created fractal 
    bitmap.show() 

def fractal2():
    height = 640
    width = 480
    image = np.zeros((height,width,3), np.uint8)

    randomNumbers = []
    size = int(random.random() *5)
         
    for randomIndex in range(size):
        randomNumbers.append(random.random())

    randomNumbersIndex = 0
    maxRandomize = height


    for x in range(width): 
        randomIndexSearch = 0
        for y in range(height):
            if randomIndexSearch > maxRandomize:
                randomIndexSearch = 0
                if(randomNumbersIndex >= size-1):
                    randomNumbersIndex = 0
                else:
                    randomNumbersIndex = randomNumbersIndex+1

            randomNumber = randomNumbers[randomNumbersIndex]

            b = ((x**2 + y**2)/randomNumber ) % 125
            g = ((x**2 + y**2)*randomNumber) % 255
            r = ((x**2+ y**2)+randomNumber )% 255
            image[y,x,0] = b
            image[y,x,1] = g
            image[y,x,2] = r

            randomIndexSearch = randomIndexSearch+1

    return image
def fractal3():
    height = 640
    width = 480
    image = np.zeros((height,width,3), np.uint8)

    b = 0
    g = 0
    r = 0
    for x in range(width): 
        for y in range(height):
            b = ((x**2 + y**2)**2) % 255
            g = ((x**2 + y**2)**2) % 255
            r = ((x**2+ y**2)**2) % 255
            image[y,x,0] = b
            image[y,x,1] = g
            image[y,x,2] = r

    return image

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
            r = (((x**2)+ (y**2))**power)*constant% 255
            image[y,x,0] = b
            image[y,x,1] = g
            image[y,x,2] = r

    return image

def fractal4():
    height = 640
    width = 480
    image = np.zeros((height,width,3), np.uint8)

    b = 1
    b2 = 1
    g = 1
    g2 = 1
    r = 1
    r2 = 1
    for x in range(width): 
        b = (b+b2) 
        g = (g+g2) 
        r = (r+r2) 
        for y in range(height):
            image[y,x,0] = b % 255
            image[y,x,1] = g % 255
            image[y,x,2] = r % 255
        b2 = b
        r2 = r
        g2 = g

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
