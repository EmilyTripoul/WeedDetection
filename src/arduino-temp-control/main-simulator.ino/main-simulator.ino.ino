
int inputControlPin = 4; // Send High to heat the water
int outputSwitchPin = 7; // Send High to open the switch
int outputControlPin = LED_BUILTIN; // Send High when the water is hot
int inputResistanceAnalog = A0; // Send High to heat the water

#define COMMAND_MODE_PIN 1
#define COMMAND_MODE_SERIAL 2
#define COMMAND_MODE COMMAND_MODE_SERIAL

#define COMMAND_MAX_LENGTH 255
char command[COMMAND_MAX_LENGTH];
int commandLength;

int inputControlState = 0;

#define TEMPERATURE_HOT_MIN 70
#define TEMPERATURE_HOT_MAX 85

class RestistanceTemp {
  public:
  RestistanceTemp() {
    resistance=0;
    temp=0;
  };
    float resistance;
    float temp;
  };

#define RESISTANCE_MAP_SIZE 16
RestistanceTemp resistanceMap[RESISTANCE_MAP_SIZE];

void setResistanceMap() {
  resistanceMap[0].resistance=900;
  resistanceMap[0].temp=24;
  resistanceMap[1].resistance=861;
  resistanceMap[1].temp=30;
  resistanceMap[2].resistance=820;
  resistanceMap[2].temp=40;
  resistanceMap[3].resistance=781;
  resistanceMap[3].temp=50;
  resistanceMap[4].resistance=730;
  resistanceMap[4].temp=54;
  resistanceMap[5].resistance=692;
  resistanceMap[5].temp=60;
  resistanceMap[6].resistance=653;
  resistanceMap[6].temp=65;
  resistanceMap[7].resistance=622;
  resistanceMap[7].temp=70;
  resistanceMap[8].resistance=585;
  resistanceMap[8].temp=75;
  resistanceMap[9].resistance=544;
  resistanceMap[9].temp=80;
  resistanceMap[10].resistance=529;
  resistanceMap[10].temp=83;
  resistanceMap[11].resistance=507;
  resistanceMap[11].temp=85;
  resistanceMap[12].resistance=492;
  resistanceMap[12].temp=87;
  resistanceMap[13].resistance=482;
  resistanceMap[13].temp=89;
  resistanceMap[14].resistance=472;
  resistanceMap[14].temp=91;
  resistanceMap[15].resistance=462;
  resistanceMap[15].temp=93;
}

float mapResitanceToTemp(int resistance) {
  if(resistance >= resistanceMap[0].resistance) {
    return resistanceMap[0].temp;
  } else if (resistance <= resistanceMap[RESISTANCE_MAP_SIZE-1].resistance) {
    return resistanceMap[RESISTANCE_MAP_SIZE-1].temp;
  }
  else {
  int mapIndex=0;
    for(int i=0;i<RESISTANCE_MAP_SIZE-1;i++) {
      if (resistance <= resistanceMap[i].resistance && resistance >= resistanceMap[i+1].resistance) {
        mapIndex=i;
        break;
      }
    }
    return resistanceMap[mapIndex].temp + (resistanceMap[mapIndex+1].temp-resistanceMap[mapIndex].temp)*static_cast<float>(resistance-resistanceMap[mapIndex].resistance)/(resistanceMap[mapIndex+1].resistance-resistanceMap[mapIndex].resistance);
  }  
}

void resetCommand() {
  for(int i =0;i<COMMAND_MAX_LENGTH;i++) {
    command[i]=0; //Could use memset
  }
  commandLength=0;
}

void readCommand() {
  while (Serial.available() >0) {
		char data = Serial.read();
    if(commandLength<COMMAND_MAX_LENGTH-1 && data != '\n') {
      command[commandLength]=data;
      commandLength++;
    }
  }  
  
  if(commandLength<COMMAND_MAX_LENGTH) {
    command[commandLength]='\0';
  }
}


void setup() { 
  
  Serial.begin(9600);     

  pinMode(inputControlPin, INPUT);  
  pinMode(inputResistanceAnalog, INPUT);  
  
  pinMode(outputSwitchPin, OUTPUT);  
  pinMode(outputControlPin, OUTPUT);  

  setResistanceMap();

  resetCommand();
 }

void displayValue(int opcode, int value) {
  char msg[255];
  sprintf(msg, "R%d V%d", opcode, value);
  Serial.println(msg);   
}

float getTemperature() {
  int resistance = 1023-analogRead(inputResistanceAnalog);
  return mapResitanceToTemp(resistance);  
}
 
int checkTemperature() {
  float temperature = getTemperature();
  return (temperature < TEMPERATURE_HOT_MIN) ? -1 : (
            (temperature > TEMPERATURE_HOT_MAX) ? 1 : 0);  
}
 
 #define COMMAND_SET_HEAT 85
 #define COMMAND_GET_HEAT 85
 
int interpretCommand() {
  if(commandLength==0) {
    return;
  }
}

int parseSegment(int startingPosition, char* currentParsingType, int* currentParsingOpcode) {
  int currentParsingPosition=startingPosition;
  int opcode=0;
  *currentParsingType='\0';
  *currentParsingOpcode=0;

  while(currentParsingPosition<commandLength && command[currentParsingPosition]==' ') {
    currentParsingPosition++;
  }
  
  if(commandLength>currentParsingPosition+1) {
    *currentParsingType = command[currentParsingPosition];
    currentParsingPosition+=1;
  } else {
    return currentParsingPosition;
  }

  for(int i=currentParsingPosition; i<commandLength;i++) {
    if(command[i]==' ' || command[i]=='\0') {
      break;
    }
    opcode=10*opcode+(command[i]-'0');
    currentParsingPosition++;
  }
  *currentParsingOpcode=opcode;
  return currentParsingPosition;
}

void loop() { 
  int checkTemperatureResult = checkTemperature();

  // Serial communication 
  #if COMMAND_MODE == COMMAND_MODE_SERIAL
    resetCommand();
    readCommand();
    
    if(commandLength>0) {
      int currentParsingPosition=0;
      char currentParsingType='\0';
      int currentParsingOpcode=0;

      currentParsingPosition=parseSegment(currentParsingPosition, &currentParsingType, &currentParsingOpcode);
      if(currentParsingType=='F') {
        if(currentParsingOpcode==85) {          
          currentParsingPosition=parseSegment(currentParsingPosition, &currentParsingType, &currentParsingOpcode);
          if(currentParsingType=='V') {
            inputControlState=currentParsingOpcode;
          }
        } else if (currentParsingOpcode==86) {
          displayValue(42, checkTemperatureResult>=0);
        } else if (currentParsingOpcode==87) {
          displayValue(43, int(getTemperature()));
        }else if (currentParsingOpcode==88) {
          displayValue(44, analogRead(inputResistanceAnalog));
        }else if (currentParsingOpcode==89) {
          displayValue(45, (inputControlState == 1) && (checkTemperatureResult<=0));
        }else if (currentParsingOpcode==90) {
          displayValue(46, inputControlState );
        }
      }
    }
  #endif
  // Pin communication 
  #if COMMAND_MODE == COMMAND_MODE_PIN
    inputControlState = digitalRead(inputControlPin);  
  #endif

  

  // Handle Ready
  if(checkTemperatureResult>=0) {
    digitalWrite(outputControlPin, HIGH);
  } else {
    digitalWrite(outputControlPin, LOW);    
  }

  // Handle Swich  
  if(inputControlState == 1 && checkTemperatureResult<=0) {
    digitalWrite(outputSwitchPin, HIGH);       
  } else {
    digitalWrite(outputSwitchPin, LOW);        
  }        

  delay(100);
}
  
