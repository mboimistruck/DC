/*
DGFN1131
Post-lab 5
Michael Boimistruck
Nov 28, 2017
*/

void setup() {
  for(int i = 13; i > 9; i--){
    pinMode(i, OUTPUT); // set up the 4 LEDs for outputs
  }
  Serial.begin(9600);
}

void loop() {
  for(int i = 0; i < 4; i++){ // make each cycle 4 blinks  
      for(int i = 10; i < 14; i++){
        digitalWrite(i, HIGH);
      }
    delay(150); // turn all 4 LEDs on, then wait 0.15 seconds
      for(int i = 10; i < 14; i++){
          digitalWrite(i, LOW);
      }
      delay(150); // turn all 4 LEDS off, then wait 0.15 seconds
    }
  delay(2000); // wait 2 seconds between cycles
}

