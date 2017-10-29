#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.write(0);
  myservo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i < 180; i++) {
    myservo.write(i);
    delay(10);
  }
  for(int i = 0; i > 0; i=i-1) {
    myservo.write(i);
    delay(10);
  }
}
