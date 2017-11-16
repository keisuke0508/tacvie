const int data_num = 2;
const int vib_pin = 9;
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
  val = Serial.read();
}

void actuate_vibration() {
  analogWrite(vib_pin, val);
  Serial.print("speed: ");
  Serial.println(val);
}
