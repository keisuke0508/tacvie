const int vib_pin = 9;
const int fan_pin = 3;
int vib_val = 0;
int fan_val = 0;;

void setup() {
  // put your setup code here, to run once:
  pinMode(vib_pin, OUTPUT);
  pinMode(fan_pin, OUTPUT);
  Serial.begin(9600);
  Serial.flush();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    get_data();
  }
  actuate_vibration();
  actuate_fan();
}

void get_data() {
  vib_val = Serial.read();
}

void actuate_vibration() {
  analogWrite(vib_pin, vib_val);
  Serial.print("speed: ");
  Serial.println(vib_val);
}

void actuate_fan() {
  if(vib_val == 0) {
    fan_val = 0;
  }else {
    fan_val = 255;
  }
  analogWrite(fan_pin, fan_val);
  Serial.print("wind: ");
  Serial.println(fan_val);
}

