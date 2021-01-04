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
  #print image
  #convert an image to grayscale
  #apply median blur
  #Retrieve the edges for cartoon effect
  #Noise removal
  #Giving a cartoon effect
  #Ploting the final transition
  
  #finished on listing all the steps to be done in this function
  #To figure out code about each step in next sitting
