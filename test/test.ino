#include <LiquidCrystal.h>
#include <string.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

char delimiter = '|';
String data;
int buzzerpin = 10;
int buttonpin = 7;
int buttonState = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(buttonpin,INPUT);
  pinMode(buzzerpin,OUTPUT);
  lcd.begin(16, 2);
}

void loop() {
  // put your main code here, to run repeatedly:


  while(Serial.available())
  {
    buttonState = digitalRead(buttonpin);  
    data = Serial.readStringUntil(delimiter);

    
    if (data.startsWith("LCD-1"))
    {
      lcd.setCursor(0,0);
      lcd.print(data.substring(5));
    }
    
    else if (data.startsWith("LCD-2"))
    { 
      lcd.setCursor(0,1);
      lcd.print(data.substring(5));
    }
  

    else if (data.startsWith("State:"))
    { 
      if (data.substring(6) == "Triggered")
      {
        tone(buzzerpin,200);
      }
      else 
      {
        noTone(buzzerpin);
      }
    }


      
    if (buttonState == LOW)
    {
      Serial.println("feelgood");
    }
    
  }
}
