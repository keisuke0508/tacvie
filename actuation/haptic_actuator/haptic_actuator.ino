#include <Servo.h>

char data[10];
Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
  myservo.write(0);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  get_data();
  Serial.println(data);
  actuate_servo();
}

void get_data() {
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
  int val = atoi(data);
  if(val <= 50) {
    myservo.write(0);
  }else if(val > 50 && val <= 800) {
    val = map(val, 50, 800, 0, 180);
    myservo.write(val);
  }else {
    myservo.write(180);
  }
}

