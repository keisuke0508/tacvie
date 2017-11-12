const int data_num = 2;
const int vib_pin = 9;
char data[10];
int val = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(vib_pin, OUTPUT);
  Serial.begin(9600);
  Serial.flush();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    get_data();
  }
  actuate_vibration();
}

void get_data() {
  int num = 0;
  while(true) {
    data[num] = Serial.read();
    if(data[num] == '/') {
      data[num] = '\0';
      val = atoi(data);
      break;
    }else {
      num += 1;
    }
  }
}

void actuate_vibration() {
  analogWrite(vib_pin, val);
  Serial.print("speed: ");
  Serial.println(val);
}
