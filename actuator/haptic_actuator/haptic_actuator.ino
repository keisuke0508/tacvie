#include <Servo.h>

const int pin = 9;
char data[10];
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
  get_data();
  actuate_servo();
}

char get_data() {
  int num = 0;
  while(true) {
    if(Serial.available() > 0) {
      data[num] = Serial.read();
      if(data[num] == '/') {
        data[num] = '\0';
        break;
      }else {
        num += 1;
      }
    }
  }
}

void actuate_servo() {
  int val = atoi(data) * 2;
  Serial.println(data);
  myservo.write(val);
}

