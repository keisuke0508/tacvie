#include <Servo.h>

const int pin = 9;
int val = 0;
Servo myservo;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  myservo.attach(pin);
  myservo.write(0);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    get_data();
  }
  actuate_servo();
}

void get_data() {
  val = Serial.read();
}

void actuate_servo() {
  Serial.println(val);
  myservo.write(val);
}

