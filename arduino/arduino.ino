void setup() {
  Serial.begin(115200);
}

void loop() {
   handleSerial();
   // Everything else loop() does…
}
 
void handleSerial() {
 while (Serial.available() > 0) {
   char incomingCharacter = Serial.read();
   switch (incomingCharacter) {
     case 'S':
      Serial.println("S" + String((float)(millis() / 2 % 2000) / 100));
      break;
 
     case 'V':
      Serial.println("V14");
      break;
    }
 }
}
