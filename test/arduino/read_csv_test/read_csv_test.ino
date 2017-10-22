char data[10];
int i = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    data[i] = Serial.read();
    if(data[i] == '/') {
      data[i] = '\0';
      Serial.println(data);
      i = 0;
    }else {
      i += 1;
    }
  }
}

