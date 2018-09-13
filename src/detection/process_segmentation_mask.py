# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:58:05 2018

@author: Emily
"""

import cv2 as cv
import numpy as np

from . import utils

def segmentationMask(mask):    
    # Find background
    kernelSize=10
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(kernelSize,kernelSize))
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    
    # Marker labelling
    ret, markers = cv.connectedComponents(closing)
    
    return (ret,markers)
    