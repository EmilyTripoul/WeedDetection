# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:19:18 2018

@author: Emily
"""

import cv2 as cv
import os
import numpy as np
import pathlib
from math import *
import matplotlib.pyplot as plt
import csv

rootFolder='./'
dataFolder=rootFolder+'data/'
srcFolder=rootFolder+'src/'
databaseName='NOT-INITIALISED'
databaseFolder=dataFolder+databaseName+'/'

dataInputFolder=databaseFolder+'input/'
dataOutputFolder=databaseFolder+'output/'
dataTmpFolder=databaseFolder+'tmp/'

def openDatabase(databaseName_):      
    global databaseName, databaseFolder, dataInputFolder, dataOutputFolder, dataTmpFolder
    databaseName=databaseName_
    databaseFolder=dataFolder+databaseName+'/'
    
    dataInputFolder=databaseFolder+'input/'
    dataOutputFolder=databaseFolder+'output/'
    dataTmpFolder=databaseFolder+'tmp/'
    
    createFolderStruct(dataInputFolder)
    createFolderStruct(dataOutputFolder)
    createFolderStruct(dataTmpFolder)

    return (dataInputFolder, dataOutputFolder)

def getFilelist():
    fileList=[]
    for file in os.listdir(dataInputFolder):
        if file.endswith(".jpg") or file.endswith(".png"):
            filePath=os.path.join(dataInputFolder, file)
            fileList.append((file, filePath))
    return fileList

def createFolderStruct(path):
    print('Creating path :' + path)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    
def cv2pltFig(image,isMask=False):
    if isMask:
        return image
    else:
        return cv.cvtColor(image, cv.COLOR_BGR2RGB)

def showImage(windowName, image, isMask=False):
    height, width = image.shape[:2]
    
    sizeX=800
    sizeY=ceil(sizeX*height/width)

    fig=plt.figure(windowName)
    img=plt.imshow(cv2pltFig(image,isMask), aspect='equal')
    img.set_cmap('hot')
    plt.axis('off')
    plt.title(windowName)
    return fig
        
def extractImageCanal(image, canalNumber):    
    imageCopy = image.copy()
    if canalNumber==0:
        imageCopy[:, :, 1] = 0
        imageCopy[:, :, 2] = 0
    elif canalNumber==2:
        imageCopy[:, :, 0] = 0
        imageCopy[:, :, 2] = 0
    else: 
        imageCopy[:, :, 0] = 0
        imageCopy[:, :, 1] = 0
    return imageCopy

def saveImage(name, image, isMask=False, isTmp=False):    
    if isTmp==True:
        saveDirectory=dataTmpFolder
    else:
        saveDirectory=dataOutputFolder
    print('Saving image :'+saveDirectory+name+'.png')
    plt.savefig(saveDirectory+name+'.png', dpi= 'figure', facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=True, bbox_inches='tight', pad_inches=0,
        frameon=None)
    #cv.imwrite(saveDirectory+name+'.png',image)
    
    
def getDataFilepathFromFilepath(path):
    splitPath=path.split('/')
    fileName=''
    filePath=''
    if path[-1]=='/':
        fileName= splitPath[-2]
        filepath= '/'.join(splitPath[0:-2])
    else:
        fileName= splitPath[-1]
        filepath= '/'.join(splitPath[0:-1])
    return filepath+'/'+'.'.join(fileName.split('.')[0:-1])+'.csv'
        

def readPlantInfo(filePath):    
    plantInfoList=[]
    with open(filePath) as csvfile:
        csvreader=csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for row in csvreader:
            for field in row:                
                row[field]=int(row[field])            
            plantInfoList.append(row)  
    return plantInfoList
