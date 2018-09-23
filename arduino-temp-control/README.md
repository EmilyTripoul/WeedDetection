# Arduino-temp-control

This arduino sketch is used to control the arduino dedicated to temperature control.

A temperature asservissment is available to ensure that the temperature inside the boiler does not go above 90°C.
It is controled from a Pin or the Serial port of the arduino. A resistance is calibrated to measure the temperature throught the analog input pin A0. 

## Analog control

The arduino can be controled from the digital pin 4 to start heating the water. It outputs a signal on pin 13 (LED_BUILTIN) when the water is hot enough at 70°C. 

Another signal is control the actual boiler on pin 7.

## Serial control

We use G-Code to control the arduino. 

### Code sent to the arduino

The following code are implemented :

| G Code | OpCode | Parameters | Result  |
| ------ |:-------| :- | :-----|
| F      | 85     | V | Change the value of the control pin (0 = stop heating/1=start heating)  |
| F      | 86     | | Check if the water is hot (>70°C)|
| F      | 87     | | Read the temperature|
| F      | 88     | | Read the thermo resistance |

### Code received from the arduino

The following code are implemented :

| G Code | OpCode | Parameters | Result  |
| ------ |:-------| :- | :-----|
| R      | 42     | V | Check if the water is hot (>70°C) : 1 if it's hot / 0 if it's under 70°C |
| R      | 43     | V | The temperature inside the boiler in °C |
| R      | 44     | V | The value of the thermo resistance (between 0 and 1023) |

### Example

A basic use case would be to start heating, read the temperature then stop heating.
```
Raspberry -> Arduino : "F85 V1"   // Start heating
Raspberry -> Arduino : "F87"      // Request the temperature
Arduino -> Raspberry : "R43 V75"  // The temperature is 75°C
Raspberry -> Arduino : "F86"      // Request if the water is hot enough
Arduino -> Raspberry : "R42 V1"   // The water is hot enough
Raspberry -> Arduino : "F85 V0"   // Stop heating
```
