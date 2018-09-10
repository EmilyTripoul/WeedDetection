# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:59:18 2018

@author: Qiu
"""

import skimage.measure
import numpy as np

import utils

def analyseMarkers(markerNumber, markers):
    regionList=[]
    for index,region in enumerate(skimage.measure.regionprops(markers)):
        if region.area>=500:
            regionList.append(region)
            #print('== Region:'+str(index))
            #print('Position :' + str(region.centroid))
            #print('Area :' + str(region.area))
            #print('Bbox :' + str(region.bbox))
    return regionList

def isInContact(region, plantInfo):
    coords=region.coords
    plantMask=(coords[:,0] - plantInfo['posX'])**2 + (coords[:,1] - plantInfo['posY'])**2 < plantInfo['radius']**2
    return np.any(plantMask)

def analysePlants(markerNumber, regionList, plantInfoList):
    
    plantList=[]
    weedList=[]
    plantLabelList=set()
    weedLabelList=set([i for i in range(1,markerNumber)])
    for region in regionList:
        plantPossibilities=[]
        for plantInfo in plantInfoList:
            if isInContact(region, plantInfo):
                plantPossibilities.append(plantInfo)   
                plantLabelList.add(region.label)
            
        if len(plantPossibilities)==0:
            weedList.append(region)
        else:
            plantList.append((region, plantPossibilities))
    
    weedLabelList=list(weedLabelList-plantLabelList)
    plantLabelList=list(plantLabelList)
    
    return (plantList, weedList, weedLabelList, plantLabelList)
    