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
  #apply median blur
  #Retrieve the edges for cartoon effect
  #Noise removal
  #Giving a cartoon effect
  #Ploting the final transition
  
  #finished on listing all the steps to be done in this function
  #To figure out code about each step in next sitting
