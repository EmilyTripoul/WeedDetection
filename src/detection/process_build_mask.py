# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:54:27 2018

@author: Emily
"""

import cv2 as cv
import numpy as np

from . import utils

def makeMask(image):
    
    imageHsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    #utils.showImage("HSV", imageHsv)
    #utils.saveImage(file+'-HSV', imageHsv)
    #saveImage('HSV-H', extractImageCanal(imageHsv,0))
    #saveImage('HSV-S', extractImageCanal(imageHsv,1))
    #saveImage('HSV-V', extractImageCanal(imageHsv,2))
    
    ## Non restrictives bound :        
    #lower_red = np.array([20,50,50])
    #upper_red = np.array([80,255,255])        
    ## Restrictive bound :
    lower_green = np.array([35,60,100])
    upper_green = np.array([80,255,255])

    mask = cv.inRange(imageHsv, lower_green, upper_green)
    #utils.showImage("mask", mask)
    #utils.saveImage(file+'-mask', mask)
    
    kernelSize=10
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(kernelSize,kernelSize))
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    
    return opening