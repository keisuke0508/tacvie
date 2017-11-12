const int vib_pin = 9;
const int dc_pin = 3;

void setup() {
  // put your setup code here, to run once:
  pinMode(vib_pin, OUTPUT);
  pinMode(dc_pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(vib_pin, 255);
  analogWrite(dc_pin, 255);
  delay(1000);
  analogWrite(vib_pin, 100);
  analogWrite(dc_pin, 0);
  delay(1000);
}
