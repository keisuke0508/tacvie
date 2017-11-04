const int pin = 9;
char data[10];

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  get_data();
  actuate_vibration();
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

void actuate_vibration() {
  int val = atoi(data);
//  Serial.println(val);
  analogWrite(pin, val);
}

