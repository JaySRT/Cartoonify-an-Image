import cv2  #for image processing
import easygui  #To open the filebox
import numpy as np  #To store image
import imageio  #To read image stored at particular path. Images are stored and processed as numbers. These are taken as arrays. We will use NumPy to deal with arrays
import sys
import matplotlib.pyplot as plt  #for visualization and plotting
import os  #For OS interaction

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


""" fileopenbox opens the box to choose file
and help us store file path as string """

def upload():
  ImagePath = easygui.fileopenbox()     #fileopenbox() is the method in easyGUI module which returns the path of the chosen file as a string.
  cartoonify(ImagePath)


def cartoonify(ImagePath):
  #read the image
  originalImage = cv2.imread(ImagePath)
  originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
  #print(image)  #Image is stored in form of numbers
  
  if originalImage is None:
    print('Can not find any image. Choose approptiate file")
    sys.exit()
         
  Resized1 = cv2. resize(originalImage, (960,540))
  #plt.imshow(Resized1, cmap = 'grap')
  
  #convert an image to grayscale
  graySaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  Resized2 = cv2.resize(grayScaleImage, (960, 540))
  #plt.imshow(Resized2, cmap = 'gray')
  
  #apply median blur to smoothen an image
  smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
  Resized3 = cv2.resize(smoothGrayScale, (960, 540))
  #plt.imshow(ReSized3, cmap = 'gray')
  
  #Retrieve the edges for cartoon effect
  getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, CV2.THRESH_BINARY, 9 ,9)
  ReSized4 = cv2.ReSize(getEdge, (960, 540))
  #plt.imshow(ReSized4, cmap='gray')   
          
  #applying bilateral filter to remove noise and keep edge sharp as required
  colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
  ReSized5 = cv2.resize(colorImage, (960, 540))
  #plt.imshow(ReSized5, cmap='gray')        
  
  #Giving a cartoon effect
  #masking edged image with our "BEAUTIFY" image
  cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
  ReSized6 = cv2.resize(cartoonImage, (960, 540))
  #plt.imshow(ReSized6, cmap='gray')
  
  # Plotting the whole transition
  images=[ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]
  fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
  for i, ax in enumerate(axes.flat):
      ax.imshow(images[i], cmap='gray')
  //save button code
  plt.show()
  
#function for SAVE Button
def save(ReSized6, ImagePath):
    #saving an image using imwrite()
    newName="cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)

          
          #Not finished yet.
          
 
