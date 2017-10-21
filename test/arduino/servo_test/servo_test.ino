#include <Servo.h>

Servo myservo;
int val;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = 0;
  myservo.write(val);
  delay(1000);
  val = 180;
  myservo.write(val);
  delay(1000);
}
