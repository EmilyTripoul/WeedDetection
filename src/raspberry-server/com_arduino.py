# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 2018

@author: Emily
"""

import serial
import time

serialArduinoUno  = None

def init():
    global serialArduinoUno
    serial1 = serial.Serial('COM3', 9600, timeout=2)
    serialArduinoUno = serial1

def parseResponse(data):
    dataCopy=data.decode("utf-8") 
    response={}
    if len(data)==0:
        return response

    if len(data)>1 and dataCopy[-1]=='\n':
        dataCopy=dataCopy[0:-1]
    if len(data)>1 and dataCopy[-1]=='\r':
        dataCopy=dataCopy[0:-1]

    dataSplit = dataCopy.split(' ')
    for code in dataSplit:
        response[code[0]]=int(code[1:])

    return response

def _arduinoUnoSendOpcodeAndGetValue(opcode, default=0):
    serialArduinoUno.write(('%s\n'%(opcode)).encode('utf-8'))
    time.sleep(1e-3)
    line = serialArduinoUno.readline()
    response = parseResponse(line)
    if not 'V' in response:
        return default
    return response['V']

def setHeatControl(value):
    serialArduinoUno.write(('F85 V%d\n'%(value)).encode('utf-8'))
    time.sleep(1e-3)
    line = serialArduinoUno.readline()
    response = parseResponse(line)
    if not 'V' in response:
        return 0
    return response['V']

def getHeatTemperatureControlState():
    return _arduinoUnoSendOpcodeAndGetValue('F86',-2)

def getHeatTemperature():
    return _arduinoUnoSendOpcodeAndGetValue('F87',0)

def getHeatResistance():
    return _arduinoUnoSendOpcodeAndGetValue('F88',-1)

def getHeatIsHeating():
    return _arduinoUnoSendOpcodeAndGetValue('F89',-1)

def close():
    if serialArduinoUno != None:
        serialArduinoUno.close()

if __name__ == '__main__':
    init()
    print('Arduino initialisation...')
    time.sleep(3.0)
    setHeatControl(1)
    while True:
        
        print('Temperature : ' + str(getHeatTemperature()))
        print('isHeating : ' + str(getHeatIsHeating()))
        time.sleep(1.0)
    close()


