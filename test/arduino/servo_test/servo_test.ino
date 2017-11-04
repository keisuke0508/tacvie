#include <Servo.h>

Servo myservo;
char data[3];

void setup() {
  // put your setup code here, to run once:
  myservo.write(0);
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  servo_test_normal();
//  servo_test_random();
//  servo_test_static();
//  servo_test_serial();
}

void servo_test_normal() {
  int val = 0;
  while(val <= 90) {
    val += 1;
    myservo.write(val);
    delay(10);
  }
  while(val >= 0) {
    val = val - 1;
    myservo.write(val);
    delay(10);
  }
}

void servo_test_random() {
  int val = random(0, 180);
  myservo.write(val);
}

void servo_test_static() {
  int val = 90;
  myservo.write(val);
}

void servo_test_serial() {
  Serial.write('a');
  get_data();
  write_data();
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

void write_data() {
  int val = atoi(data);
  myservo.write(val);
  Serial.println(val);
}

