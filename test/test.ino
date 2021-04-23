#include <LiquidCrystal.h>
#include <string.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

char delimiter = '|';
String data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin(16, 2);
  
}

void loop() {
  // put your main code here, to run repeatedly:
 
  
  while(Serial.available())
  {
    
    data = Serial.readStringUntil(delimiter);
    
    if (data.startsWith("LCD-1"))
    {
      lcd.setCursor(0,0);
      lcd.print(data.substring(5));
    }
    
    else if (data.startsWith("LCD-2"))
    { 
      Serial.println("WE ARE HERE");
      lcd.setCursor(0,1);
      lcd.print(data.substring(5));
    }


  }
  
  

}
