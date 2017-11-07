const int data_num = 2;
const int vib_pin = 9;
const int fan_pin = 3;
char data[10];

void setup() {
  // put your setup code here, to run once:
  pinMode(vib_pin, OUTPUT);
  pinMode(fan_pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int data_list[2];
  for(int n = 0; n < data_num; n++) {
    get_data();
    data_list[n] = atoi(data);
  }
  actuate_vibration(data_list[0]);
  actuate_fan(data_list[1]);
  Serial.print("speed: ");
  Serial.println(data_list[0]);
  Serial.print("wind: ");
  Serial.println(data_list[1]);
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

void actuate_vibration(int val) {
//  Serial.println(val);
  analogWrite(vib_pin, val);
}

void actuate_fan(int val) {
  analogWrite(fan_pin, val);
}

