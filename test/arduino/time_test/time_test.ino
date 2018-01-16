#include <Wire.h>
#include <RTC8564ms.h>

RTC8564ms *rtc;

void setup(){
  Serial.begin(9600);
  rtc=new RTC8564ms(2);
  rtc->setTime(2018,1,16,13,30,0,0);
  
}

void loop(){
  rtc->updateTime();
  Serial.println(rtc->toString());
  delay(1000);
}
