const int vib_pin = 9;
const int fan_pin = 3;
int val = 0;

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
  val = Serial.read();
}

void actuate_vibration() {
  analogWrite(vib_pin, val);
  Serial.print("speed: ");
  Serial.println(val);
}

void actuate_fan() {
  analogWrite(fan_pin, val);
  Serial.print("wind: ");
  Serial.println(val);
}

