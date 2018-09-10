# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:24:49 2018

@author: Emily
"""

import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import cv2 as cv
from math import *
import numpy as np
import matplotlib.pyplot as plt

import utils
import process_build_mask
import process_segmentation_mask
import process_analyse_markers

utils.openDatabase('test-1')

for file, filePath in utils.getFilelist():
    print('Processing :'+filePath)

    image = cv.imread(filePath)
    utils.showImage("Original", image)
    
    mask=process_build_mask.makeMask(image)
    utils.showImage("mask", mask, True)
    utils.saveImage(file+'-mask', mask, True)
    res = cv.bitwise_and(image,image, mask= mask)
    utils.showImage("res", res)
    utils.saveImage(file+'-res', res)
    
    markerNumber, markers=process_segmentation_mask.segmentationMask(mask)
    utils.showImage("markers", markers, True)
    utils.saveImage(file+'-markers', markers, True)
        
    regionList=process_analyse_markers.analyseMarkers(markerNumber, markers)
              
    plantInfoList=utils.readPlantInfo(filePath)
    
    plantList, weedList, weedLabelList, plantLabelList=process_analyse_markers.analysePlants(markerNumber, regionList, plantInfoList)
    
    weedMask=np.isin(markers,weedLabelList)
    plantMask=np.isin(markers,plantLabelList)
    combinedMask=1*weedMask+2*plantMask
        
    fig=utils.showImage('combinedMask', combinedMask, True)
    ax=plt.gca()
    for plantInfo in plantInfoList:
        circle= plt.Circle((plantInfo['posY'], plantInfo['posX']),radius=plantInfo['radius'], color='g', fill=False, linewidth=3)
        ax.add_artist(circle)
    utils.saveImage(file+'-combinedMask', combinedMask, True)
    
    