# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:24:49 2018

@author: Emily
"""

if __name__ == '__main__':
    # Make file standalone
    import sys
    from pathlib import Path # if you haven't already done so
    file = Path(__file__).resolve()
    parent, root = file.parent, file.parents[1]
    sys.path.append(str(root))

    # Additionally remove the current file's directory from sys.path
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

import cv2 as cv
from math import *
import numpy as np
import matplotlib.pyplot as plt

from . import utils, process_build_mask, process_segmentation_mask, process_analyse_markers

def processImage(image, plantInfoList, filename='', showImage=True, outputImage=True):    
    mask=process_build_mask.makeMask(image)
    if showImage:
        utils.showImage("mask", mask, True)
        if outputImage:
            utils.saveImage(filename+'-mask', mask, True)
    #res = cv.bitwise_and(image,image, mask= mask)
    #utils.showImage("res", res)
    #utils.saveImage(filename+'-res', res)
    
    markerNumber, markers=process_segmentation_mask.segmentationMask(mask)
    if showImage:
        utils.showImage("markers", markers, True)
        if outputImage:
            utils.saveImage(filename+'-markers', markers, True)
        
    regionList=process_analyse_markers.analyseMarkers(markerNumber, markers)
                  
    plantList, weedList, weedLabelList, plantLabelList=process_analyse_markers.analysePlants(markerNumber, regionList, plantInfoList)
    
    weedMask=np.isin(markers,weedLabelList)
    plantMask=np.isin(markers,plantLabelList)
    combinedMask=1*weedMask+2*plantMask
        
    if showImage:
        fig=utils.showImage('combinedMask', combinedMask, True)
        ax=plt.gca()
        for plantInfo in plantInfoList:
            circle= plt.Circle((plantInfo['posY'], plantInfo['posX']),radius=plantInfo['radius'], color='g', fill=False, linewidth=3)
            ax.add_artist(circle)
        if outputImage:
            utils.saveImage(filename+'-combinedMask', combinedMask, True)
    
    return plantList, weedList
    
def processDatabase(databaseName):
    dataInputFolder, dataOutputFolder = utils.openDatabase(databaseName)
    plantInfoList=utils.readPlantInfo(dataInputFolder+'database.csv')
    for file, filePath in utils.getFilelist():
        print('Processing :'+filePath)

        image = cv.imread(filePath)
        utils.showImage("Original", image)
        processImage(image, plantInfoList, filename=file)

if __name__ == '__main__':
    processDatabase('test-1')