#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);




void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin(16, 2);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  String data; 
  
  while(Serial.available())
  {
    data = Serial.readString();
     lcd.print(data);
    if (data.startsWith("LCD-1"))
    {
      lcd.setCursor(0,0);
      lcd.print(data.substring(5));
    }
    
    else if (data.startsWith("LCD-2"))
    { 
      lcd.setCursor(0,1);
      Serial.print(data.substring(5));
    }
  }
  
  

}
