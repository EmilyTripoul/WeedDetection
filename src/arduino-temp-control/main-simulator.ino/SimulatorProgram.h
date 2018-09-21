#include "Arduino.h"

// Init Variabelen voor Arduino UNO simulator

int Sim_Input0 = -1;
int Sim_Input1 = -1;
int Sim_Input2 = -1;
int Sim_Input3 = -1;
int Sim_Input4 = -1;
int Sim_Input5 = -1;
int Sim_Input6 = -1;
int Sim_Input7 = -1;
int Sim_Input8 = -1;
int Sim_Input9 = -1;
int Sim_Input10 = -1;
int Sim_Input11 = -1;
int Sim_Input12 = -1;
int Sim_Input13 = -1;
int Sim_Input14 = -1;
int Sim_Input15 = -1;
int Sim_Input16 = -1;
int Sim_Input17 = -1;
int Sim_Input18 = -1;
int Sim_Input19 = -1;
int Sim_PWM_Old0 = 0;
int Sim_PWM_Old1 = 0;
int Sim_PWM_Old2 = 0;
int Sim_PWM_Old3 = 0;
int Sim_PWM_Old4 = 0;
int Sim_PWM_Old5 = 0;
int Sim_Data0;
int Sim_Data1;
int Sim_Value0;
int Sim_Value1;
int Sim_Value2;
int Sim_Value3;
int Sim_Value4;
int Sim_Value5;
int Sim_Dummy00 = 0;
int Sim_Dummy01 = 1;
int Sim_DummyAna = 0;
String inString = "";
boolean stringComplete = false;
String Str1;
String Str2;
int Sim_Read_out0 = 0;
int Sim_Read_out1 = 0;
int Sim_Read_out2 = 0;
int Sim_Read_out3 = 0;
int Sim_Read_out4 = 0;
int Sim_Read_out5 = 0;
int Sim_Read_out6 = 0;
int Sim_Read_out7 = 0;
int Sim_Read_out8 = 0;
int Sim_Read_out9 = 0;
int Sim_Read_out10 = 0;
int Sim_Read_out11 = 0;
int Sim_Read_out12 = 0;
int Sim_Read_out13 = 0;
int Sim_Read_out14 = 0;
int Sim_Read_out15 = 0;
int Sim_Read_out16 = 0;
int Sim_Read_out17 = 0;
int Sim_Read_out18 = 0;
int Sim_Read_out19 = 0;
String Sim_Rij = "tx1";
String Sim_Kol = "";
String Sim_Kolom = "";
int Sim_Kolom1 = 0;
int Sim_Scroll = 0;
String Sim_Scrolla;
String Sim_Scrollb;



//*************************************************************************************************************************************************************************************************
//********************** START PROGRAM ARDUINO UNO SIMULATOR //START PROGRAM ARDUINO UNO SIMULATOR //START PROGRAM ARDUINO UNO SIMULATOR //START PROGRAM ARDUINO UNO SIMULATOR ********************
//*************************************************************************************************************************************************************************************************

// SerialEvent occurs whenever a new data comes in the hardware serial RX.  This routine is run between each time loop() runs, so using delay inside loop can delay
// response.  Multiple bytes of data may be available.

   void serialEvent() {
      while (Serial.available()) {              // get the new byte:
        char inChar = (char)Serial.read();
        inString += inChar;                     // add it to the inString:
        if (inChar == '\n') {                   // if the incoming character is a newline, set a flag so the main loop can do something about it:
          stringComplete = true;
          Str1 = inString.substring(0,3);
          Str2 = inString.substring(3,7);
        }   
        
     //////////////////////////////////// KEUZE INPUTS //////////////////////////////////////
     
     if (stringComplete == true) {                              // Ontvangen van character 'LF'
       if((Str1 == "I00")&&(Str2 == "1111")){                    // Input knop 0 (Start)
         Sim_Input0 = 1;
       }else if((Str1 == "I00")&&(Str2 == "0000")){              // Input knop 0 (Stop)
         Sim_Input0 = -1; 
       }  
       if((Str1 == "I01")&&(Str2 == "1111")){                    // Input knop 1 (Input)
         Sim_Input1 = 1;
       }else if((Str1 == "I01")&&(Str2 == "0000")){              // Input knop 1 (Stop)
         Sim_Input1 = -1; 
       }   
       if((Str1 == "I02")&&(Str2 == "1111")){                    // Input knop 2 (Input)
         Sim_Input2 = 1;
       }else if((Str1 == "I02")&&(Str2 == "0000")){              // Input knop 2 (Stop)
         Sim_Input2 = -1; 
       }              
       if((Str1 == "I03")&&(Str2 == "1111")){                    // Input knop 3 (Input)
         Sim_Input3 = 1;
       }else if((Str1 == "I03")&&(Str2 == "0000")){              // Input knop 3 (Stop)
         Sim_Input3 =-1;
       }
       if((Str1 == "I04")&&(Str2 == "1111")){                    // Input knop 4 (Input)
         Sim_Input4 = 1;
        }else if((Str1 == "I04")&&(Str2 == "0000")){           // Input knop 4 (Stop)
         Sim_Input4 = -1;
       }       
       if((Str1 == "I05")&&(Str2 == "1111")){                    // Input knop 5 (Input)
         Sim_Input5 = 1;
       }else if((Str1 == "I05")&&(Str2 == "0000")){              // Input knop 5 (Stop)
         Sim_Input5 = -1;
       }       
       if((Str1 == "I06")&&(Str2 == "1111")){                    // Input knop 6 (Input)
         Sim_Input6 = 1;
       }else if((Str1 == "I06")&&(Str2 == "0000")){              // Input knop 6 (Stop)
         Sim_Input6 = -1; 
       }       
       if((Str1 == "I07")&&(Str2 == "1111")){                    // Input knop 7 (Input)
         Sim_Input7 = 1;
       }else if((Str1 == "I07")&&(Str2 == "0000")){              // Input knop 7 (Stop)
         Sim_Input7 = -1; 
       }       
       if((Str1 == "I08")&&(Str2 == "1111")){                    // Input knop 8 (Input)
         Sim_Input8 = 1;
       }else if((Str1 == "I08")&&(Str2 == "0000")){              // Input knop 8 (Stop)
         Sim_Input8 = -1; 
       }       
       if((Str1 == "I09")&&(Str2 == "1111")){                    // Input knop 9 (Input)
         Sim_Input9 = 1;
       }else if((Str1 == "I09")&&(Str2 == "0000")){              // Input knop 9 (Stop)
         Sim_Input9 = -1; 
       } 
       if((Str1 == "I10")&&(Str2 == "1111")){                    // Input knop 10 (Input)
         Sim_Input10 = 1;
       }else if((Str1 == "I10")&&(Str2 == "0000")){              // Input knop 10 (Stop)
         Sim_Input10 = -1; 
       }             
       if((Str1 == "I11")&&(Str2 == "1111")){                    // Input knop 11 (Input)
         Sim_Input11 = 1;
       }else if((Str1 == "I11")&&(Str2 == "0000")){              // Input knop 11 (Stop)
         Sim_Input11 = -1; 
       } 
        if((Str1 == "I12")&&(Str2 == "1111")){                   // Input knop 12 (Input)
         Sim_Input12 = 1;
       }else if((Str1 == "I12")&&(Str2 == "0000")){              // Input knop 12 (Stop)
         Sim_Input12 = -1; 
       }       
        if((Str1 == "I13")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input13 = 1;
       }else if((Str1 == "I13")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input13 = -1; 
       }   
       if((Str1 == "I14")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input14 = 1;
       }else if((Str1 == "I14")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input14 = -1; 
       }   
       if((Str1 == "I15")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input15 = 1;
       }else if((Str1 == "I15")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input15 = -1; 
       }   
       if((Str1 == "I16")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input16 = 1;
       }else if((Str1 == "I16")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input16 = -1; 
       }   
       if((Str1 == "I17")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input17 = 1;
       }else if((Str1 == "I17")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input17 = -1; 
       }   
       if((Str1 == "I18")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input18 = 1;
       }else if((Str1 == "I18")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input18 = -1; 
       }   
       if((Str1 == "I19")&&(Str2 == "1111")){                   // Input knop 13 (Input)
         Sim_Input19 = 1;
       }else if((Str1 == "I19")&&(Str2 == "0000")){              // Input knop 13 (Stop)
         Sim_Input19 = -1; 
       }   
       
       ///////////////////////////////// KEUZE ANALOGE INPUTS ////////////////////////////////// 
       
       if(Str1 == "A00"){  // Analoge ingang 0
         Sim_Value0 = (Str2.toInt()); 
         if (Str2 == "1111"){ 
          Serial.print("A001111"); 
          delay(10); // pause 10ms
          Serial.print('\n');
         }
       }
        if(Str1 == "A01"){  // Analoge ingang 1
         Sim_Value1 = (Str2.toInt()); 
         if (Str2 == "1111"){  
           Serial.print("A011111"); 
           delay(10); // pause 10ms
           Serial.print('\n'); 
         }   
       }
        if(Str1 == "A02"){  // Analoge ingang 2
         Sim_Value2 = (Str2.toInt()); 
         if (Str2 == "1111"){   
           Serial.print("A021111"); 
           delay(10); // pause 10ms
           Serial.print('\n');
         }    
       }
        if(Str1 == "A03"){  // Analoge ingang 3
         Sim_Value3 = (Str2.toInt()); 
           if (Str2 == "1111"){   
           Serial.print("A031111"); 
           delay(10); // pause 10ms
           Serial.print('\n'); 
         }   
       }
        if(Str1 == "A04"){  // Analoge ingang 4
         Sim_Value4 = (Str2.toInt()); 
         if (Str2 == "1111"){ 
           Serial.print("A041111"); 
           delay(10); // pause 10ms
           Serial.print('\n'); 
         }   
       }
        if(Str1 == "A05"){  // Analoge ingang 5
         Sim_Value5 = (Str2.toInt()); 
         if (Str2 == "1111"){   
           Serial.print("A051111"); 
           delay(10); // pause 10ms
           Serial.print('\n');
         }    
       }
       
       ///////////////////////////////   KEUZE PWM OMVORMERS   /////////////////////////////////
       
       if(Str1 == "P03"){  // Select PWM 0 (3) door Java Simulator
         Serial.print("P031111"); 
         delay(10); // pause 10ms
         Serial.print('\n'); 
       }
       if(Str1 == "P05"){  // Select PWM 1 (5) door Java Simulator
         Serial.print("P051111");          
         delay(10); // pause 10ms
         Serial.print('\n');      
       }
       if(Str1 == "P06"){  // Select PWM 2 (6) door Java Simulator
         Serial.print("P061111");         
         delay(10); // pause 10ms
         Serial.print('\n');         
       }
       if(Str1 == "P09"){  // Select PWM 3 (9) door Java Simulator
         Serial.print("P091111");          
         delay(10); // pause 10ms
         Serial.print('\n');        
       }
       if(Str1 == "P10"){  // Select PWM 4 (10) door Java Simulator
         Serial.print("P101111");          
         delay(10); // pause 10ms
         Serial.print('\n');         
       }
       if(Str1 == "P11"){  // Select PWM 5 (11) door Java Simulator
         Serial.print("P11");          
         delay(10); // pause 10ms
         Serial.print('\n');            
       } 
       if (stringComplete) {
         inString = "";                     // clear the string:
         stringComplete = false;
       }           
     } 
   } 
 }  
////////////////////////// EINDE ONTVANGEN/ZENDEN SERIELE COMMUNICATIE /////////////////////////////
 
////////////////////////////////////////////// Functies ///////////////////////////////////////////
//////////////////////////////////////// Functie digitalWrite /////////////////////////////////////
 int DigitalWrite(int pin, int High){
   Sim_Dummy00 = 0;
   Sim_Dummy01 = 0;
   switch (pin) {
    case 0:if ((High == HIGH)&&(Sim_Read_out0 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out0 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out0 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out0 = 0;
              }        
              break;    
    case 1:if ((High == HIGH)&&(Sim_Read_out1 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out1 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out1 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out1 = 0;
              }        
              break;    
    case 2:if ((High == HIGH)&&(Sim_Read_out2 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out2 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out2 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out2 = 0;
              }        
              break;    
    case 3:if ((High == HIGH)&&(Sim_Read_out3 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out3 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out3 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out3 = 0;
              }        
              break;    
    case 4:if ((High == HIGH)&&(Sim_Read_out4 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out4 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out4 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out4 = 0;
              }        
              break;    
    case 5:if ((High == HIGH)&&(Sim_Read_out5 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out5 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out5 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out5 = 0;
              }        
              break;    
    case 6:if ((High == HIGH)&&(Sim_Read_out6 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out6 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out6 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out6 = 0;
              }        
              break;    
    case 7:if ((High == HIGH)&&(Sim_Read_out7 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out7 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out7 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out7 = 0;
              }        
              break;    
    case 8:if ((High == HIGH)&&(Sim_Read_out8 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out8 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out8 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out8 = 0;
              }        
              break;    
     case 9:if ((High == HIGH)&&(Sim_Read_out9 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out9 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out9 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out9 = 0;
              }        
              break;    
     case 10:if ((High == HIGH)&&(Sim_Read_out10 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out10 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out10 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out10 = 0;
              }        
              break;    
     case 11:if ((High == HIGH)&&(Sim_Read_out11 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out11 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out11 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out11 = 0;
              }        
              break;    
     case 12:if ((High == HIGH)&&(Sim_Read_out12 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out12 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out12 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out12 = 0;
              }        
              break;    
     case 13:if ((High == HIGH)&&(Sim_Read_out13 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out13 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out13 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out13 = 0;
              }        
              break; 
     case 14:if ((High == HIGH)&&(Sim_Read_out14 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out14 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out14 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out14 = 0;
              }        
              break;    
     case 15:if ((High == HIGH)&&(Sim_Read_out15 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out15 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out15 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out15 = 0;
              }        
              break;    
     case 16:if ((High == HIGH)&&(Sim_Read_out16 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out16 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out16 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out16 = 0;
              }        
              break;    
     case 17:if ((High == HIGH)&&(Sim_Read_out17 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out17 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out17 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out17 = 0;
              }        
              break; 
    case 18:if ((High == HIGH)&&(Sim_Read_out18 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out18 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out18 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out18 = 0;
              }        
              break;       
    case 19:if ((High == HIGH)&&(Sim_Read_out19 == 0)){            
             Sim_Dummy01 = 1;
             Sim_Read_out19 = 1;
            }   
            if ((High == LOW)&&(Sim_Read_out19 == 1)){             
              Sim_Dummy00 = 1; 
              Sim_Read_out19 = 0;
              }        
              break;             
           }  // END CASE
           if (Sim_Dummy01 == 1){            
            if (pin <= 9) {
              String Sim_Data0 = String("O0"+String(pin)+"1111");      //"00?1111"  met ?= 0 tem 9
              Serial.print(Sim_Data0);
              }else {
              String Sim_Data0 = String("O"+String(pin)+"1111");      //"0?1111"  met ?= 10 tem 19
              Serial.print(Sim_Data0);
              }
              delay(20);                                              // pause 100ms     
              Serial.print('\n');  
              delay(10);                          
              Sim_Dummy01 = 0;
            }   
            if (Sim_Dummy00 == 1){             
              if (pin <= 9) {
               String Sim_Data0 = String("O0"+String(pin)+"0000");     //"00?0000"  met ?= 0 tem 9
               Serial.print(Sim_Data0);
               }else {
               String Sim_Data0 = String("O"+String(pin)+"0000");     //"0?0000"  met ?= 10 tem 19
               Serial.print(Sim_Data0);
               }
               delay(20);                                            // pause 100ms
               Serial.print('\n'); 
               delay(10);                                             // pause 10ms
               Sim_Dummy00 = 0;
         }                       
     }

//////////////////////////////////////// Functie digitalRead //////////////////////////////////////
 int DigitalRead(int pin){
   serialEvent();
   int result; 
   if (pin == A0){
     pin = 14;  
   }
   if (pin == A1){
     pin = 15;  
   }
   if (pin == A2){
     pin = 16;  
   }
   if (pin == A3){
     pin = 17;  
   }
   if (pin == A4){
     pin = 18;  
   }
   if (pin == A5){
     pin = 19;  
   }      
   switch (pin) {
    case 0:if (Sim_Input0 == 1){
            result = 1;
           }   
           if (Sim_Input0 == -1){
            result = 0;
           }       
      break;
    case 1:if (Sim_Input1 == 1){
            result = 1;
           }
           if (Sim_Input1 == -1){
            result = 0;
           }             
      break;
    case 2:if (Sim_Input2 == 1){
            result = 1;
           } 
           if (Sim_Input2 == -1){
            result = 0;
           }            
      break;
    case 3:if (Sim_Input3 == 1){
            result = 1;
           } 
           if (Sim_Input3 == -1){
            result = 0;
           }            
      break;
    case 4:if (Sim_Input4 == 1){
            result = 1;
           } 
           if (Sim_Input4 == -1){
            result = 0;
           }            
      break;   
    case 5:if (Sim_Input5 == 1){
            result = 1;
           }
           if (Sim_Input5 == -1){
            result = 0;
           }            
      break; 
    case 6:if (Sim_Input6 == 1){
            result = 1;
           } 
           if (Sim_Input6 == -1){
            result = 0;
           }            
      break; 
    case 7:if (Sim_Input7 == 1){
            result = 1;
           }
           if (Sim_Input7 == -1){
            result = 0;
           }            
      break; 
    case 8:if (Sim_Input8 == 1){
            result = 1;
           }
           if (Sim_Input8 == -1){
            result = 0;
           } 
      break;  
    case 9:if (Sim_Input9 == 1){
            result = 1;
           }
           if (Sim_Input9 == -1){
            result = 0;
           }            
      break; 
    case 10:if (Sim_Input10 == 1){
            result = 1;
           }
           if (Sim_Input10 == -1){
            result = 0;
           }            
      break;
    case 11:if (Sim_Input11 == 1){
            result = 1;
           } 
           if (Sim_Input11 == -1){
            result = 0;
           }            
      break;
    case 12:if (Sim_Input12 == 1){
             result = 1;
           }
           if (Sim_Input12 == -1){
             result = 0;
           }            
      break;  
    case 13:if (Sim_Input13 == 1){
             result = 1;
           }
           if (Sim_Input13 == -1){
             result = 0;
           }            
      break; 
    case 14:if (Sim_Input14 == 1){
             result = 1;
           }
           if (Sim_Input14 == -1){
             result = 0;
           }            
      break;     
    case 15:if (Sim_Input15 == 1){
             result = 1;
           }
           if (Sim_Input15 == -1){
             result = 0;
           }            
      break;     
    case 16:if (Sim_Input16 == 1){
             result = 1;
           }
           if (Sim_Input16 == -1){
             result = 0;
           }            
      break;     
    case 17:if (Sim_Input17 == 1){
             result = 1;
           }
           if (Sim_Input17 == -1){
             result = 0;
           }            
      break;     
    case 18:if (Sim_Input18 == 1){
             result = 1;
           }
           if (Sim_Input18 == -1){
             result = 0;
           }            
      break;     
    case 19:if (Sim_Input19 == 1){
             result = 1;
           }
           if (Sim_Input19 == -1){
             result = 0;
           }            
      break;         
  }
    return result;  
 }  

//////////////////////////////////////// Functie analogWrite //////////////////////////////////////
 int AnalogWrite(int pin ,int PWMwaarde){
   Sim_DummyAna = 0;
   switch (pin) {
    case 3:if (PWMwaarde != Sim_PWM_Old0){      // Nieuw <> Oud
              Sim_PWM_Old0 = PWMwaarde;
              Sim_DummyAna = 1;
           }
           break;
    case 5:if (PWMwaarde != Sim_PWM_Old1){      // Nieuw <> Oud
              Sim_PWM_Old1 = PWMwaarde;
              Sim_DummyAna = 1;
           }
           break; 
    case 6:if (PWMwaarde != Sim_PWM_Old2){      // Nieuw <> Oud
              Sim_PWM_Old2 = PWMwaarde;
              Sim_DummyAna = 1;
           }
           break;
    case 9:if (PWMwaarde != Sim_PWM_Old3){      // Nieuw <> Oud
              Sim_PWM_Old3 = PWMwaarde;
              Sim_DummyAna = 1;
           }
           break;
    case 10:if (PWMwaarde != Sim_PWM_Old4){      // Nieuw <> Oud
              Sim_PWM_Old4 = PWMwaarde;
              Sim_DummyAna = 1;
           }
           break;  
    case 11:if (PWMwaarde != Sim_PWM_Old5){      // Nieuw <> Oud
              Sim_PWM_Old5 = PWMwaarde;
              Sim_DummyAna = 1;
           }
           break;     
    }    // END CASE
   if (Sim_DummyAna == 1){
    if (pin <= 9) {
      String Sim_Data0 = String("P0"+String(pin)+PWMwaarde);
      Serial.print(Sim_Data0);
     }else {
      String Sim_Data0 = String("P"+String(pin)+PWMwaarde);
      Serial.print(Sim_Data0);
     }
     delay(20);  
     Serial.print('\n'); 
     delay(10);  // pause 10ms
    }
 }
 
///////////////////////////////////////// Functie analogRead //////////////////////////////////////
 int AnalogRead(int pin){
   serialEvent();
   int result;
   result = 0;
   if (((pin == A0)||(pin == 0))&&(Sim_Value0 < 1111)){
     result = Sim_Value0; 
   }
   if (((pin == A1)||(pin == 1))&& (Sim_Value1 < 1111)){
     result = Sim_Value1; 
   }
   if (((pin == A2)||(pin == 2))&&(Sim_Value2 < 1111)){
     result = Sim_Value2; 
   }
   if ((pin == A3)||(pin == 3)&&(Sim_Value3 < 1111)){
      result = Sim_Value3; 
   }
   if ((pin == A4)||(pin == 4)&&(Sim_Value4 < 1111)){
      result = Sim_Value4; 
   }
   if ((pin == A5)||(pin == 5)&&(Sim_Value5 < 1111)){
      result = Sim_Value5; 
   }  
   return result; 
 }
 
///////////////////////////////////////// Functie servo ///////////////////////////////////////////
int myservowrite(int servo){
  String Sim_Data0 = String("S12 "+ String (servo));
  Serial.print(Sim_Data0); 
  delay(20);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}
////////////////////////////////////// Functie tone en noTone ////////////////////////////////////
int Tone(int pin, int freq , int tijd){
  String Sim_Data0 = String("TF" + String(pin) + String(freq));      // TF = Tone Frequentie
  Serial.print(Sim_Data0); 
  delay(20);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms  
  String Sim_Data1 = String("TT" + String(pin) + String(tijd));      // TT = Tone Tijd
  Serial.print(Sim_Data1); 
  delay(20);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms  
}

int NoTone(int pin){
  String Sim_Data0 = String("END0000");              // END = Stop de tone
  Serial.print(Sim_Data0); 
  delay(20);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
} 

/////////////////////////////////////// Functie Serialprint ////////////////////////////////////
int Serialprint(String text){
  Serial.print("txt" + text); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms   
}

/////////////////////////////////////// Functie lcdsetCursor ////////////////////////////////////
int lcdsetCursor(int kolom , int rij){
  Serial.print("SPX1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
  Sim_Kolom1 = kolom;
  String Sim_Data0 = String (Sim_Kolom1);
  if (rij == 0) {
    Sim_Rij = "tx1";              // LCD display bovenste rij
    Serial.print("SP1" + Sim_Data0); 
  }else {
    Sim_Rij = "tx2";              // LCD display onderste rij
    Serial.print("SP2" + Sim_Data0); 
  }  
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
  Sim_Kol = "                ";   // 16 kolommen spaties   
}
/////////////////////////////////////// Functie lcdprint ////////////////////////////////////
int lcdLprint(long text){                          // Versturen van een long integer
  Serial.print("PRL1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
  Sim_Kol = "                ";   // 16 kolommen spaties
  if (Sim_Rij == "tx2") {
    Sim_Rij = "tx2";
  }else {
    Sim_Rij = "tx1";
    Sim_Kolom1 = 0;
  }
  Sim_Scrolla = Sim_Kol.substring(0, Sim_Kolom1);  // Berekenen aantal spaties voor verschuiven tekst
  String Sim_Data0 = String (text);   
  Serial.print(Sim_Rij + Sim_Scrolla + Sim_Data0);    //Serial.print(Sim_Rij + Sim_Scrolla + Sim_Data0); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
}
int lcdprint(String text){                        // Versturen van een string  
  Serial.print("PRT1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
  Sim_Kol = "                ";   // 16 kolommen spaties
  if (Sim_Rij == "tx2") {
    Sim_Rij = "tx2";
  }else {
    Sim_Rij = "tx1";
    Sim_Kolom1 = 0;
  }
  Sim_Scrolla = Sim_Kol.substring(0, Sim_Kolom1);  // Berekenen aantal spaties voor verschuiven tekst
  Serial.print(Sim_Rij + Sim_Scrolla + text);     // Serial.print(Sim_Rij + Sim_Scrolla + text);
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms   
  Sim_Kolom1 = Sim_Kolom1 - Sim_Scroll ; 
}

////////////////////////////////////// Functie lcdautoscroll ///////////////////////////////////
int lcdautoscroll(){
  Sim_Scroll = 1; 
  Serial.print("SCR1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms    
}
int lcdnoAutoscroll(){
  Sim_Scroll = 0; 
  Serial.print("SCR0000"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms    
}

///////////////////////////////////////// Functie lcdclear /////////////////////////////////////
int lcdclear(){ 
  Serial.print("CLR1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms    
}

/////////////////////////////////////// Functie lcddisplay //////////////////////////////////
int lcddisplay(){
  Serial.print("YDP1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}
/////////////////////////////////////// Functie lcdnoDisplay //////////////////////////////////
int lcdnoDisplay(){
  Serial.print("NDP1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}

///////////////////////////////////////// Functie lcdblink ///////////////////////////////////
int lcdblink(){
  Serial.print("YBL1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
}

///////////////////////////////////////// Functie lcdnoBlink ///////////////////////////////////
int lcdnoBlink(){
  Serial.print("NBL1111"); 
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}

///////////////////////////////////////// Functie lcdwrite ////////////////////////////////////
int lcdwrite(char text){
  Serial.print("YWR1111");
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
  
  String Sim_Data0 = String (Sim_Kolom1);
  Sim_Kol = "                ";   // 16 kolommen spaties
  if (Sim_Rij == "tx2") {
    Sim_Rij = "tx2";
    Serial.print("SP2" + Sim_Data0);
  }else {
    Sim_Rij = "tx1";
    Sim_Kolom1 = 0;
    Serial.print("SP1" + Sim_Data0);
  }
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
  
  Sim_Scrolla = Sim_Kol.substring(0, Sim_Kolom1);  // Berekenen aantal spaties voor verschuiven tekst   
  Serial.print(Sim_Rij + Sim_Scrolla + text);     // Serial.print(Sim_Rij + Sim_Scrolla + text);
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms       
  Sim_Kolom1 = Sim_Kolom1 - Sim_Scroll ; 
}

///////////////////////////////////////// Functie lcdright to left ////////////////////////////////////
int lcdrightToLeft(){
  Serial.print("RTL1111");
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
}

///////////////////////////////////////// Functie lcdleft to right ////////////////////////////////////
int lcdleftToRight(){
 Serial.print("LTR1111");
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms  
}

//////////////////////////////////////////// Functie lcdhome /////////////////////////////////////////
int lcdhome(){
  Serial.print("HOM1111");
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms 
}

//////////////////////////////////////////// Functie lcdcursor /////////////////////////////////////////
int lcdcursor(){
  if (Sim_Rij == "tx2") {
    Sim_Rij = "tx2";
    Serial.print("CUR2222");
  }else {
    Sim_Rij = "tx1";
    Serial.print("CUR1111");
  }
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}

////////////////////////////////////// Functie lcdscrollDisplayLeft ///////////////////////////////////
int lcdscrollDisplayLeft(){
  Serial.print("SDL1111");
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}

////////////////////////////////////// Functie lcdscrollDisplayRight ///////////////////////////////////
int lcdscrollDisplayRight(){
  Serial.print("SDR1111");
  delay(10);  
  Serial.print('\n'); 
  delay(10);  // pause 10ms
}

//*************************************************************************************************************************************************************************************************
//************************ END PROGRAM ARDUINO UNO SIMULATOR //END PROGRAM ARDUINO UNO SIMULATOR //END PROGRAM ARDUINO UNO SIMULATOR //END PROGRAM ARDUINO UNO SIMULATOR **************************
//************************************************************************************************************************************************************************************************* 
