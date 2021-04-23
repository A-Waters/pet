int data;
int LED=13;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED,HIGH);
  Serial.println("Hellow how are you");
}

void loop() {
  // put your main code here, to run repeatedly:


  while(Serial.available())
  {
    data = Serial.read();
    Serial.print(data);
    if (data == '1')
      digitalWrite(LED,HIGH);
    else
      digitalWrite(LED,LOW);
  }

  

}
